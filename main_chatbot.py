import ollama


# Import file path if Knowledge base is needed
with open('/home/unearnedlogic/Desktop/AI/INOVA/Knowledge base.txt', 'r') as kb:
    my_base = kb.read()


# Store previous messages in a list
conversation_history = [{"role": "system", "content": my_base}]


def chat_with_ai(user_input):
    # Add the user's question to the history
    conversation_history.append({"role": "user", "content": user_input})

    # Send the entire history to Ollama
    response = ollama.chat(model="llama3.2", messages=conversation_history)

    # Store AI response in history
    ai_response = response["message"]["content"]
    conversation_history.append({"role": "assistant", "content": ai_response})

    return ai_response

while True:
    user_input = input('Write to AI - ')
    if user_input == '/bye':
        break
    else:
        print(chat_with_ai(user_input))
        print()
