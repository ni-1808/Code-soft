import re  #using RedEX module to write more code in single without using loop
import datetime
import random

# Here is The Facts list that can show you facts when you chat with bot
facts = [
    "Octopuses have three hearts.",
    "Bananas are berries, but strawberries aren't.",
    "The Eiffel Tower can grow taller in summer.",
    "Honey never spoils.",
    "A day on Venus is longer than its year."
]

print("ChatBot: Hello! I am a rule based chatbot.Ask me anything or type 'exit' to end the conversation.")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if re.search(r"\b(exit|quit|bye|goodbye|thanks)\b", user_input):
        print("ChatBot: Conversation ended. Take care!")
        break

    # Greeting
    elif re.search(r"\b(hello|hi|hey|greetings|good morning|good evening)\b", user_input):
        print("ChatBot: Hello there! What would you like to know today?")

    # Weather
    elif re.search(r"\b(weather|forecast|rain|sunny|temperature|climate)\b", user_input):
        print("ChatBot: Weather is ever-changing. Please check a local weather app for accurate info.")

    # Actual time
    elif re.search(r"\b(time|current time|what time)\b", user_input):
        now = datetime.datetime.now()
        print(f"ChatBot: The current time is {now.strftime('%I:%M %p')}.")

    # Actual date
    elif re.search(r"\b(date|day|today)\b", user_input):
        today = datetime.date.today()
        print(f"ChatBot: Today’s date is {today.strftime('%A, %B %d, %Y')}.")

    # Help
    elif re.search(r"\b(help|support|assist|guidance|need help)\b", user_input):
        print("ChatBot: I can tell you the date, time, fun facts, or answer basic math questions.")

    # Identity
    elif re.search(r"\b(who|your name|identify|who are you)\b", user_input):
        print("ChatBot: I'm a simple rule-based chatbot built to assist with general queries.")

    # Math operations like "what is 5 + 3"
    elif re.search(r"what\s+is\s+(\d+)\s*([\+\-\*/])\s*(\d+)", user_input):
        match = re.search(r"what\s+is\s+(\d+)\s*([\+\-\*/])\s*(\d+)", user_input)
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))
        result = None

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = round(num1 / num2, 2) if num2 != 0 else "undefined (division by zero)"

        print(f"ChatBot: The result is {result}.")

    # Fun fact
    elif re.search(r"\b(fact|interesting|tell me something|funny)\b", user_input):
        fact = random.choice(facts)
        print(f"ChatBot: Did you know? {fact}")

    # Fallback for unrecognized input
    else:
        responses = [
            "ChatBot: I'm not sure how to respond to that.",
            "ChatBot: Try asking me about the time, date, or a math question.",
            "ChatBot: Interesting... but I don't have a reply for that.",
            "ChatBot: Could you ask something simpler?"
        ]
        print(random.choice(responses))