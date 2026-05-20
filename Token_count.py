import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load .env
load_dotenv()

# Create client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def optimize_prompt_with_llm(long_prompt):
    """Uses the LLM to rewrite a long prompt into a concise, structured version."""
    print("🔄 Prompt is too long! Routing to the Prompt Optimizer Agent...\n")

    # System instruction forces the LLM to act as a prompt engineer
    optimizer_instruction = """
    You are an expert prompt engineer. Your job is to take the user's lengthy, 
    conversational input and rewrite it into a highly concise, structured prompt.
    Use bullet points if necessary. Remove all filler words, pleasantries, and unnecessary context.
    RETURN ONLY THE REWRITTEN PROMPT. DO NOT ANSWER THE ACTUAL QUESTION.
    """

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=long_prompt,
        config=types.GenerateContentConfig(
            system_instruction=optimizer_instruction,
            temperature=0.1  # Very low temperature for strict, analytical rewriting
        )
    )

    return response.text


def run_smart_query(user_prompt):
    word_count = len(user_prompt.split())

    # ---------------------------------------------------------
    # 1. EVALUATE & OPTIMIZE (The "Agentic" Routing Step)
    # ---------------------------------------------------------
    if word_count < 3:
        print(f"⚠️ Prompt too vague ('{user_prompt}'). Please provide more details.")
        return

    elif word_count > 30:  # Threshold for triggering the optimizer
        final_prompt = optimize_prompt_with_llm(user_prompt)
        print(f"✨ Optimized Prompt:\n{final_prompt}\n")
    else:
        final_prompt = user_prompt
        print(f"Sending original prompt: '{final_prompt}'...\n")

    # ---------------------------------------------------------
    # 2. FINAL API CALL (Answering the Question)
    # ---------------------------------------------------------
    print("🤖 Generating Final Answer...")
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=final_prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are a strict, highly efficient assistant. Provide direct, concise answers without filler text.",
            temperature=0.3
        )
    )

    print("--- Model Response ---")
    print(response.text)
    print("----------------------\n")

    # ---------------------------------------------------------
    # 3. TOKEN USAGE (For the Final Call)
    # ---------------------------------------------------------
    usage = response.usage_metadata
    print("--- Token Usage (Final Call) ---")
    print(f"Prompt Tokens:    {usage.prompt_token_count}")
    print(f"Response Tokens:  {usage.candidates_token_count}")
    print(f"Total Consumed:   {usage.total_token_count}")


# --- Testing the Logic ---

print("=== TEST: The Agentic Optimizer ===")
# A highly conversational, bloated prompt (over 30 words)
bloated_prompt = """
Hello there! I hope you are having a wonderful day today. I was just sitting here 
wondering about programming languages, and I wanted to ask if you could possibly 
explain to me what exactly the main differences are between Python and Java? I need 
to know for a project, so any help would be super appreciated. Thank you so much!
"""

run_smart_query(bloated_prompt)