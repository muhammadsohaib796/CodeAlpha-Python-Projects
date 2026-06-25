#Simple Chatbot!
def chatbot(user_choice):
    user_choice = user_choice.lower()
    
    if "hello" in user_choice or "hi" in user_choice:
        return "Hello! How  can i help you today?"
    elif "how are you" in user_choice:
        return "I'm doing great thanks for asking."
    elif "your name" in user_choice:
        return "I am Simple python chatbot!"
    elif "age" in user_choice:
        return "I don't have age like humans."
    elif "bye" in user_choice:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry! i didn't understand that"
print("Wellcome to our chatbot")
print("Chatbot: Hello! Type something (type bye to exit)")       

while True:
    user = input("You: ")
    response = chatbot(user)
    print("Chatbot: ",response)
    if "bye" in user.lower():
        break
