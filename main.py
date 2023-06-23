import openai
import os
import sys
import json

try:
  openai.api_key = os.environ['OPENAI_API_KEY']
except KeyError:
  sys.stderr.write("""
    You haven't set up your API key yet.

    If you don't have an API key yet, visit:

    https://platform.openai.com/signup

    1. Make an account or sign in
    2. Click "View API Keys" from the top right menu.
    3. Click "Create new secret key"

    Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
    """)
  exit(1)


def add_numbers(a, b):
  return a + b


def subtract_numbers(a, b):
  return a - b


def chat_with_assistant(messages, functions=None):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",  # Replace with "gpt-4" if you have early access
    messages=messages,
    functions=functions,
    function_call="auto")
  return response.choices[0].message


# Start the conversation with a system message
messages = [{"role": "system", "content": "You are a helpful assistant."}]

functions = [{
  "name": "add_numbers",
  "description": "Add two numbers",
  "parameters": {
    "type": "object",
    "properties": {
      "a": {
        "type": "number",
        "description": "First number"
      },
      "b": {
        "type": "number",
        "description": "Second number"
      },
    },
    "required": ["a", "b"],
  },
}, {
  "name": "subtract_numbers",
  "description": "Subtract two numbers",
  "parameters": {
    "type": "object",
    "properties": {
      "a": {
        "type": "number",
        "description": "First number"
      },
      "b": {
        "type": "number",
        "description": "Second number"
      },
    },
    "required": ["a", "b"],
  },
}]

print(
  "You can start chatting with the assistant. Type 'exit' to end the conversation."
)

while True:
  user_message = input("User: ")
  if user_message.lower() == 'exit':
    break

  messages.append({"role": "user", "content": user_message})

  assistant_response = chat_with_assistant(messages, functions)

  if assistant_response.get("function_call"):
    function_name = assistant_response["function_call"]["name"]
    function_args = json.loads(
      assistant_response["function_call"]["arguments"])

    print(f"Function called: {function_name}")

    if function_name == "add_numbers":
      result = add_numbers(function_args["a"], function_args["b"])
    elif function_name == "subtract_numbers":
      result = subtract_numbers(function_args["a"], function_args["b"])

    print(f"Function result: {result}")

    messages.append({
      "role": "function",
      "name": function_name,
      "content": str(result)
    })
    assistant_response = chat_with_assistant(messages, functions)

  print(f"Assistant: {assistant_response['content']}")

  messages.append(assistant_response)
