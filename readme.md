# GPT Function Playground

This repository contains a simple Python playground for testing the custom function functionality of OpenAI's GPT models, such as gpt-3.5-turbo and gpt-4. The code demonstrates how to use the Chat Completions API to define and call custom functions using the model's generated responses.

The sample code includes a basic chatbot that can perform addition and subtraction using user-defined functions. It showcases how to define functions, send them to the Chat Completions API, check if the model wants to call a function, execute the function, and send the function response back to the model.

## Requirements

- Python 3.6 or later
- OpenAI Python package: `pip install openai`

## Setup

1. Clone this repository.
2. Obtain an API key from OpenAI by signing up at https://platform.openai.com/signup.
3. Set the OPENAI_API_KEY environment variable with your API key.
4. Run `python main.py` and start chatting with the assistant.

## Usage

- Type your messages as input to interact with the chatbot.
- Ask the assistant to perform addition or subtraction, for example:
  - "What's the sum of 5 and 3?"
  - "Subtract 7 from 10."
- Type 'exit' to end the conversation.

## Extending the Code

Feel free to modify the code and add your own custom functions. To do so, follow these steps:

1. Define your new function in the code.
2. Add the function definition to the `functions` list, including the name, description, and parameters.
3. Update the function call handling section of the code to execute your new function when it's called by the model.

Remember to follow the guidelines and limits of the Chat Completions API when defining and using custom functions. Enjoy experimenting with the GPT Function Playground!