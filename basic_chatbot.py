
# Function to generate chatbot responses
def chatbot_response(user_input):

    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi":
        return "Hello! How can I help you?"

    elif user_input == "how are you":
        return "I am fine, thanks! How are you?"

    elif user_input == "what is your name":
        return "I am a simple Python chatbot."

    elif user_input == "what can you do":
        return "I can chat with you and answer simple questions."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that."


# Main program
print("Chatbot: Hello! Welcome to my chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:

    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Chatbot:", response)

    if user_input.lower() == "bye":
        break
