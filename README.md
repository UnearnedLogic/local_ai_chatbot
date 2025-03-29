# AI Chatbot Using Ollama

## Overview
This project implements a simple AI chatbot using the Ollama library. The chatbot maintains a conversation history and provides responses based on an optional knowledge base stored in a text file.

## Prerequisites
- Python 3.x
- Ollama library installed

## Installation
### Install Ollama
To install Ollama, follow these steps:
1. Visit the official website: [https://ollama.com/](https://ollama.com/)
2. Download and install Ollama for your operating system (Windows, macOS, or Linux).
3. Follow the setup instructions provided on the website.

### Install Python Dependencies
1. Install the required dependencies:
   ```bash
   pip install ollama
   ```

## Usage
Run the script to start chatting with the AI:
```bash
python chatbot.py
```

### How It Works
1. The script optionally loads a knowledge base from `Knowledge base.txt` if it exists.
2. It initializes a conversation history, starting with the system's base knowledge (if provided).
3. The `chat_with_ai` function:
   - Adds user input to the conversation history.
   - Sends the conversation history to the Ollama model (`llama3.2`).
   - Stores the AI's response in the history.
   - Returns the AI's response.
4. The chatbot runs in a loop, continuously accepting user input and generating responses.

## Example Interaction
```
User: Hello
AI: Hello! How can I assist you today?
User: What is AI?
AI: AI stands for Artificial Intelligence, which refers to the simulation of human intelligence in machines.
```

## Notes
- Modify the `model="llama3.2"` parameter if you want to use a different model.
- If no knowledge base file is found, the chatbot will still function but may have limited contextual knowledge.

## License
This project is licensed under the MIT License.

