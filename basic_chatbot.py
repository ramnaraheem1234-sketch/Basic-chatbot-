def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! 👋"

    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! 😊"

    elif user_input in ["what is your name"]:
        return "I'm a basic chatbot created in Python."

    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Have a nice day! 👋"

    elif user_input in ["thanks", "thank you"]:
        return "You're welcome! 😊"

    else:
        return "Sorry, I don't understand that."

# Main program
print("🤖 Basic Chatbot (type 'exit' to quit)")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    response = chatbot_response(user_input)
    print("Bot:", response)