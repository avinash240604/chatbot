def get_user_input():
    """Gets input from the user."""
    return input("You: ").lower().strip()

def get_bot_response(user_input):
    """Returns a predefined response based on user input."""
    responses = {
        "hello": "Hi!",
        "what is your name": "My name is ChatBot.",
        "how are you": "I'm fine, thanks! What about you?",
        "can you do any operations": "No! I'm a simple chatbot.",
        "generate animal images": "Sorry! I'm not an AI tool.",
        "chatbot means": "A simple communication tool.",
        "bye": "Goodbye!"
    }

    return responses.get(user_input, "Sorry, I don't understand that.")

def chat():
    """Main function to run the chatbot loop."""
    print("ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user_input = get_user_input()
        response = get_bot_response(user_input)
        print("ChatBot:", response)

        if user_input == "bye":
            break

# Run the chatbot
chat()
