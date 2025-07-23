import math

layout = [' ' for _ in range(9)]

def display_board():
    print("\n")
    for i in range(3):
        row = layout[i*3:(i+1)*3]
        print(" | ".join(row))
        if i < 2:
            print("---+---+---")
    print("\n")

def winner(brd):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for x, y, z in win_combos:
        if brd[x] == brd[y] == brd[z] and brd[x] != ' ':
            return brd[x]
    if ' ' not in brd:
        return "Draw"
    return None

def remaning_spots(brd):
    return [i for i in range(9) if brd[i] == ' ']

def minimax(brd, is_max, ai_player, human_player):
    result = winner(brd)
    if result == ai_player:
        return 1
    elif result == human_player:
        return -1
    elif result == "Draw":
        return 0

    if is_max:
        best = -math.inf
        for move in remaning_spots(brd):
            brd[move] = ai_player
            score = minimax(brd, False, ai_player, human_player)
            brd[move] = ' '
            best = max(best, score)
        return best
    else:
        best = math.inf
        for move in remaning_spots(brd):
            brd[move] = human_player
            score = minimax(brd, True, ai_player, human_player)
            brd[move] = ' '
            best = min(best, score)
        return best

def ai_steps(ai_player, human_player):
    best_score = -math.inf
    best_move = None
    for move in remaning_spots(layout):
        layout[move] = ai_player
        score = minimax(layout, False, ai_player, human_player)
        layout[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    layout[best_move] = ai_player

def human_steps(human_player):
    while True:
        try:
            move = int(input("Choose your move (1-9): ")) - 1
            if move in remaning_spots(layout):
                layout[move] = human_player
                break
            else:
                print("That spot is taken or invalid.")
        except ValueError:
            print("Please enter a number from 1 to 9.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    human = ''
    while human not in ['X', 'O']:
        human = input("Choose your symbol (X or O): ").upper()
    ai = 'O' if human == 'X' else 'X'
    current_turn = 'X'

    while True:
        display_board()
        if current_turn == human:
            human_steps(human)
        else:
            print("AI is thinking...")
            ai_steps(ai, human)

        result = winner(layout)
        if result:
            display_board()
            if result == "Draw":
                print("It's a draw!")
            elif result == human:
                print("🎉 You won!")
            else:
                print("🤖 AI won!")
            break

        current_turn = ai if current_turn == human else human

if __name__ == "__main__":
    main()
