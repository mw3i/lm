import sys
import os
import platform

import openai
import dotenv
dotenv.load_dotenv('env')
dotenv.load_dotenv('.secrets')

# # # # # 
# SETUP
# # # # # 
if len(sys.argv) < 2:
    print("No message provided. Usage: hey <message>")
    sys.exit(1)

query = " ".join(sys.argv[1:])

# Get the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY", None)

# Check if a file "os/history" exists, if not, make one.
history_file = "os/history"
if not os.path.exists(history_file):
    with open(history_file, 'w') as file:
        file.write('')

# Open the file and read the content (saved to variable history)
with open(history_file, 'r') as file:
    history = file.read()


# # # # # 
# PROMPT
# # # # # 
prompt = f"""
A user is currently using a terminal; they have an issue they need your help with. Provide a solution to their problem. The conversation so far:

---
{history}
---

Their system platform is: {platform.system()}
Their shell is: {os.getenv('SHELL', '?')}

Your solution must work for that system configuration.

Tell the user what to do. Keep your answer very very brief; do not provide explanations. Just describe what the user should do, and end your message with the terminal command you want them to type in.

Here is the user's question:
{query}
"""

# # # # # 
# API CALL
# # # # # 
# Initialize the OpenAI client; make request
openai.api_key = api_key
client = openai.OpenAI()
try:
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        stream=True,
    )
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)


# # # # # 
# PRINT RESPONSE TO TERMINAL
# # # # # 
# Print response
print("\n------")
print("LLM RESPONSE")
print("------\n")
response = ''
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="") 
            # print(content, end='', flush=True)  # Print the content as it arrives
    response += chunk.choices[0].delta.content or ""
print("\n\n------")
print("------")

# Append "user: <query>" and "system: <response>" lines to the history file
with open(history_file, "a") as f:
    f.write(f"\nuser: {query}\n")
    f.write(f"system: {response}\n")

# Keep only the last 100 lines in the history file
with open(history_file, "r") as f:
    lines = f.readlines()

# Write back only the last 100 lines
with open(history_file, "w") as f:
    f.writelines(lines[-int(os.getenv('OK_HISTORY_SIZE', 20)):])