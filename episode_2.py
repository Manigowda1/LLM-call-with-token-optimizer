import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Empty conversation history
messages = []

# First user message
user_input_1 = "Who is Virat Kohli?"

messages.append(
    {
        "role": "user",
        "parts": [{"text": user_input_1}]
    }
)

# Generate response
response_1 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=messages
)

# Store assistant response
messages.append(
    {
        "role": "model",
        "parts": [{"text": response_1.text}]
    }
)

print(response_1.text)

# Second user message
user_input_2 = "How many centuries did he make?"

messages.append(
    {
        "role": "user",
        "parts": [{"text": user_input_2}]
    }
)

# Generate second response
response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=messages
)

print(response_2.text)