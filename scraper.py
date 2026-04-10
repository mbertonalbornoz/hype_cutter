import requests
from bs4 import BeautifulSoup
from smolagents import tool, CodeAgent, LiteLLMModel, DuckDuckGoSearchTool


@tool
def scrape_reddit_or_web(url: str) -> str:
    """
    Scrapes the content of a webpage or a Reddit thread. 
    Use this to get 'The Reality' from specific threads or review articles.

    Args:
        url: The full URL of the page to scrape.
    """
    headers = {"User-Agent": "MarketScout/1.0 (Macintosh; Intel Mac OS X 10_15_7)"}

    # Logic to handle Reddit specifically for cleaner data
    if "reddit.com" in url:
        # We use old.reddit.com because it's easier to parse without JS
        url = url.replace("www.reddit.com", "old.reddit.com")

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        # Get text and clean up whitespace
        text = soup.get_text(separator=' ')
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = '\n'.join(chunk for chunk in chunks if chunk)

        # Return only the first 3000 characters to stay within context limits
        return clean_text[:3000]

    except Exception as e:
        return f"Error scraping {url}: {str(e)}"


# --- Re-Initialize the Agent with the new tool ---

# model = LiteLLMModel(
#     model_id="ollama_chat/deepseek-r1:32b",
#     api_base="http://localhost:11434"
# )
#
# MARKET_SCOUT_PROMPT = """You are the Market Scout. Use search to find links,
# then use the 'scrape_reddit_or_web' tool to read the actual discussions."""
#
# agent = CodeAgent(
#     tools=[DuckDuckGoSearchTool(), scrape_reddit_or_web],
#     model=model,
#     description=MARKET_SCOUT_PROMPT
# )
#
# # Test it out!
# agent.run(
#     "Is the Dyson Airwrap worth the price for someone with thin hair? Check Reddit for actual long-term durability.")