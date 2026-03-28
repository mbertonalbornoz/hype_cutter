from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
from scraper import scrape_reddit_or_web
from save_to_desktop import save_report_to_desktop

# 1. Setup the Local Model (pointing to your Ollama instance)
# Ensure you ran 'ollama run deepseek-r1:32b' first!
model = LiteLLMModel(
    model_id="ollama_chat/deepseek-r1:32b",
    api_base="http://localhost:11434", # Default Ollama port
    num_ctx=8192 # Giving it a decent memory window
)

SYSTEM_PROMPT = """
    You are Market Scout, a cynical but fair product researcher. 
    Your goal is to find the "ground truth" about products by comparing official 
    specs/marketing with raw user sentiment from Reddit, specialized forums, and 
    independent review sites.

    When a user asks about a product:
    1. Search for recent (last 12 months) Reddit threads and expert reviews.
    2. Identify "The Hype" (what the brand claims).
    3. Identify "The Reality" (common points of failure or user complaints).
    4. Assign a "Bullshit Meter" score from 1-10 (1 = Honest, 10 = Pure Marketing).
    5. Conclude with a "Buy, Wait, or Skip" recommendation.

    Tone: Professional, analytical, and slightly skeptical. Avoid flowery language.
"""

# 2. Define the Agent's Tools
# We'll start with a free, no-API-key-required search tool.
search_tool = DuckDuckGoSearchTool()

# 3. Initialize the Agent
agent = CodeAgent(
    tools=[search_tool, scrape_reddit_or_web, save_report_to_desktop],
    model=model,
    add_base_tools=True, # Gives the agent a built-in Python interpreter
    description=SYSTEM_PROMPT
)

task = "Should I buy the Renpho 3 massage gun?"

# 4. Run your first test
print("--- Market Scout is investigating ---")
result = agent.run(f"{SYSTEM_PROMPT}\n\nTask: {task}")

print("\n--- FINAL REPORT ---")
print(result)