print("Welcome to Python World")

response = {
    "hi": "Hi, How can I help you",
    "how are you": "I am fine. Thanks for asking",
    "who are you": "I am a chatbot created by Obito",
    "bye": "GoodBye to you also, Have a nice day"
}

def get_response(user_input):
    cleaned_input = user_input.lower().strip()
    
    for key in response:
        if key in cleaned_input:
            return response[key]
            
    return "Sorry! I did not understand the question."

# Take user input
while True:
    user_input = input("Please ask your question: ")
    
    if "bye" in user_input.lower():
        print("Bot : GoodBye to you also, Have a nice day.....")
        break
        
    reply = get_response(user_input)
    print("Bot :", reply)