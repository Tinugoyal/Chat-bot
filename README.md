print("🤖 Chatbot: Hello! I’m your chatbot. Type 'bye' to end the chat.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("🤖 Chatbot: Hello there! How can I help you?")
    elif "name" in user_input:
        print("🤖 Chatbot: I’m Chatbot 1.0, created by Tinu!")
    elif "do" in user_input:
        print("🤖 Chatbot: I can chat with you and answer simple questions.")
    elif "creator" in user_input:
        print("🤖 Chatbot: I am created by Mr.Tinu Goyal")
    elif "help" in user_input:
        print("🤖 Chatbot: according to my limit")
    elif  "you" in user_input:
        print("🤖 Chatbot: I am ok!")
    elif user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a nice day 😊")
        break
    else:
        print("🤖 Chatbot: I didn’t understand that. Try asking something else.")
