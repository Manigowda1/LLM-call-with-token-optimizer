# LLM Call with Token Optimizer

An intelligent prompt optimizer and token tracker for building cost-effective Agentic workflows using the Google GenAI SDK. 

## Features
* **Direct LLM Calls**: Basic interaction with the Gemini 2.5 Flash model.
* **Agentic Prompt Routing**: Intercepts bloated or vague user prompts and uses a specialized "Prompt Engineer" LLM agent to rewrite them for maximum token efficiency.
* **Token Tracking**: Extracts and displays exactly how many tokens were used in both the prompt and the response.

## Setup Instructions
1. Ensure you have Python and `uv` installed.
2. Clone this repository to your local machine.
3. Run `uv sync` to automatically build your virtual environment and install dependencies.
4. Create a `.env` file in the root directory and add your API key:
   `GEMINI_API_KEY="your_api_key_here"`
5. Run the scripts using `uv run python <script_name>.py`.

## Files
* `FirstLLM_Call.py`: A foundational script demonstrating basic LLM interaction.
* `Token_Count.py`: The core agentic script featuring the prompt-optimizing routing logic.
