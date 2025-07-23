import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

# === Load Data ===
@st.cache_data
def load_data():
    ratings = pd.read_csv("ml-100k/u.data", sep="\t", names=["user_id", "movie_id", "rating", "timestamp"])
    movies = pd.read_csv("ml-100k/u.item", sep="|", encoding="latin-1", names=[
        "movie_id", "title", "release_date", "video_release_date", "IMDb_URL",
        "unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime",
        "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
        "Romance", "Sci-Fi", "Thriller", "War", "Western"
    ])
    return ratings, movies

ratings, movies = load_data()

# === Collaborative Filtering Function ===
def collaborative_filtering_recommend(user_id, k=5):
    # Create user-item matrix
    user_movie_matrix = ratings.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)

    # Compute user similarity
    user_sim = cosine_similarity(user_movie_matrix)
    user_sim_df = pd.DataFrame(user_sim, index=user_movie_matrix.index, columns=user_movie_matrix.index)

    # Find k most similar users
    sim_users = user_sim_df[user_id].drop(user_id).sort_values(ascending=False).head(k)

    # Get ratings of similar users
    sim_user_ratings = user_movie_matrix.loc[sim_users.index]

    # Weighted sum of ratings
    weighted_ratings = sim_user_ratings.T.dot(sim_users)

    # Normalize by sum of similarities
    similarity_sum = sim_users.sum()
    predicted_ratings = weighted_ratings / similarity_sum

    # Remove already rated movies
    already_rated = user_movie_matrix.loc[user_id][user_movie_matrix.loc[user_id] > 0].index
    predicted_ratings = predicted_ratings.drop(already_rated, errors='ignore')

    # Top N recommendations
    top = predicted_ratings.sort_values(ascending=False).head(10)
    return movies.set_index("movie_id").loc[top.index][['title']]

# === Streamlit UI ===
st.title("🎥 Movie Recommender System (Collaborative Filtering)")
user_input = st.number_input("Enter User ID (1 - 943)", min_value=1, max_value=943, value=1, step=1)

if st.button("Get Recommendations"):
    recommendations = collaborative_filtering_recommend(user_input)
    st.subheader("Recommended Movies:")
    st.table(recommendations.reset_index(drop=True))
