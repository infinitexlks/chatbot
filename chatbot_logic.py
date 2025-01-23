import random

# Basic responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm doing great, thanks for asking!", "I'm just a bot, but I'm functioning well!"],
    "bye": ["Goodbye! Take care.", "See you later!", "Bye! Have a great day!"],
    "default": ["Sorry, I don't understand that.", "Can you rephrase that?", "Hmm, I didn't get that."]
}

def get_response(user_input):
    user_input = user_input.lower()  # Convert to lowercase for simplicity
    return random.choice(responses.get(user_input, responses["default"]))
