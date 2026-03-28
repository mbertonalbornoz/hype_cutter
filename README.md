# 🕵️‍♂️ Hype Cutter (Market Scout)

Hype Cutter is an AI agent designed to find the "ground truth" about products. It uses the `smolagents` Python package to search the web, scrape official specs and marketing claims, and compare them with raw user sentiment from Reddit, specialized forums, and independent review sites.

The agent, nicknamed **Market Scout**, is professional, analytical, and slightly cynical. It identifies "The Hype" vs. "The Reality", assigns a "Bullshit Meter" score, and provides a final recommendation.

## 🚀 Features

-   **Web Searching:** Uses DuckDuckGo to find recent reviews and specs.
-   **Content Scraping:** Specially handles Reddit (via old.reddit.com) and other web pages to extract clean text.
-   **AI Analysis:** Powered by local LLMs via Ollama (default: `deepseek-r1:32b`).
-   **Multiple Interfaces:** Choose between a CLI-based run or a Streamlit web UI.
-   **Report Export:** Save reports directly to your Desktop (CLI) or download them (UI).

## 🛠️ Stack

-   **Language:** Python 3.12+
-   **Package Manager:** [uv](https://github.com/astral-sh/uv) (recommended)
-   **Frameworks:** `smolagents` (Hugging Face), `LiteLLM`, `Streamlit`
-   **Search/Scraping:** `duckduckgo-search`, `BeautifulSoup4`, `requests`
-   **LLM Provider:** [Ollama](https://ollama.com/) (Local)

## 📋 Requirements

1.  **Python 3.12+**
2.  **Ollama:** Installed and running locally.
3.  **Local Model:** Pull the default model used in the code:
    ```bash
    ollama pull deepseek-r1:32b
    ```
    *(Note: You can change the `model_id` in `app.py` or `scout_ui.py` if you wish to use a different/smaller model.)*

## ⚙️ Setup

Using `uv` (recommended):
```bash
uv sync
```

Alternatively, using `pip`:
```bash
pip install -r pyproject.toml # or install dependencies listed in pyproject.toml
```

## 🏃 Commands & Entry Points

### 1. Web Interface (Streamlit)
The most user-friendly way to use Market Scout.
```bash
uv run streamlit run scout_ui.py
```

### 2. CLI Test
Run a quick investigation defined in `app.py`.
```bash
uv run app.py
```

### 3. Individual Component Tests
-   **Scraper Test:** `uv run scraper.py` (runs a test search for Dyson Airwrap)

## 📂 Project Structure

-   `scout_ui.py`: Streamlit-based web interface.
-   `app.py`: Main entry point for CLI-based agent execution.
-   `scraper.py`: Contains the `scrape_reddit_or_web` tool for content extraction.
-   `save_to_desktop.py`: Tool for saving Markdown reports to the macOS Desktop.
-   `pyproject.toml` & `uv.lock`: Project metadata and dependency management.

## 🌐 Environment Variables
*No specific environment variables are required by default as it uses local Ollama.* 
If you switch to a cloud provider via LiteLLM (e.g., OpenAI, Anthropic), you will need to set their respective API keys (e.g., `OPENAI_API_KEY`).

## 🧪 Tests
-   Currently, tests are performed by running the scripts directly (e.g., `app.py` or `scraper.py`).
-   TODO: Implement a formal testing suite using `pytest`.

