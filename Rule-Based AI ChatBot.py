import time
print("Hello! Welcome to AI ChatBot ")
print("I am here to help you with some Basic Questions")
print("Type 'Bye' anytime to Exit")
uname=input("Enter your name: ")
chat={
    "hello":"Hello, How may I help you",
    "who are you":"I am AI ChatBot",
    "give a motivational quote":"Be the Change that you Wish to See in the World",
    "what is python":"Python is a programming language",
    "happy":"Good, You should be Happy",
    "sad":"Forget the Past,Don't worry about the Future, Just Live in the Present",
    "tell me a joke":"Why do programmers prefer Dark Mode? \n Because Light attracts Bugs😄",
    "prefer me a book about money":"I Prefer you 'The Psychology of Money' Book",
    "ask me a riddle":"What has Keys but can't open locks? \n Answer Piano",
    }
def response(userinput):
    for i in chat:
        if i == userinput:
            return chat[i]
        elif userinput=="bye":
            time.sleep(1)
            return f"Thankyou {uname} for using AI ChatBot"
            break
    return f"Sorry {uname}, I will learn this soon"
while True:
    uinput=input("Please ask your question:  ").lower()
    responses=response(uinput)
    time.sleep(1)
    print("Bot Response:  ",responses)
    if uinput == "bye":
        break