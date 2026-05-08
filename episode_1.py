import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Create client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Generate response
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How many centuries did he make?"
)

print(response.text)