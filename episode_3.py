import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Infinite loop for continuous prompts
while True:

    # Take user input
    user_prompt = input("\nEnter your prompt (type 'exit' to stop): ")

    # Stop condition
    if user_prompt.lower() == "exit":
        print("Exiting chatbot...")
        break

    # Generate response
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=user_prompt
    )

    # Print response
    print("\nAI Response:\n")
    print(response.text)