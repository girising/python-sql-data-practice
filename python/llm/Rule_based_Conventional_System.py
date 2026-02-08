#Rule-based chatbot function
"""A rule-based Systemt operates on hard-coded rules. These rules define what the system should do when it encounters specific input.
For example:
If someone says "hello", respond with "Hi there!"
If someone asks for your name, respond with "I'm a chatbot!"
This type of system does not learn or adapt — it's predictable and easy to implement, but not flexible.
You'll now create your first rule-based chatbot below."""

def rule_based_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "your name" in user_input:
        return "I am a simple rule-based chatbot."
    elif "what the wether today" in user_input:
        return "I am not sure the weather but its nice day to code"
    elif "bye" in user_input or "Good bye" in user_input:
        return "Good bye!. Have a great day!"
    else:
        return "I am not sure how to repond to that. can you rephrase"
"""Try it!
Type something like:
"Hi"
"What's your name?"
"Tell me the weather"
"Bye"
To exit the chatbot, type exit."""

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Session ended.")
        break
    response = rule_based_chatbot(user_input)
    print("Chatbot:", response)

