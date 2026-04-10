import streamlit as st
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

from save_to_desktop import save_report_to_desktop
from scraper import scrape_reddit_or_web

# ... import your previous scrape_reddit_or_web tool here ...

# --- UI CONFIG ---
st.set_page_config(page_title="Market Scout AI", page_icon="🕵️‍♂️")
st.title("🕵️‍♂️ Market Scout: Hype vs. Reality")
st.markdown("Enter a product name to generate a cynical, Reddit-backed research report.")


# --- AGENT SETUP ---
@st.cache_resource  # Keeps the model in memory so it doesn't reload every time
def get_agent():
    model = LiteLLMModel(
        model_id="ollama_chat/deepseek-r1:32b",
        api_base="http://localhost:11434"
    )
    # We remove the 'save_to_desktop' tool here because
    # we'll use Streamlit's native download button instead.
    return CodeAgent(
        tools=[DuckDuckGoSearchTool(), scrape_reddit_or_web],
        model=model,
        description="You are Market Scout. Research products and return a detailed Markdown report."
    )


agent = get_agent()

# --- THE INTERFACE ---
product_query = st.text_input("What product are you suspicious of?", placeholder="e.g. Rabbit R1, Dyson Airwrap...")

if st.button("Start Investigation"):
    if product_query:
        with st.status("🔍 Scout is digging through the web...", expanded=True) as status:
            st.write("Searching for specs and marketing claims...")
            # Run the agent
            report = agent.run(f"Research the product '{product_query}'. Provide a full Hype vs Reality report.")
            status.update(label="✅ Investigation Complete!", state="complete", expanded=False)

        # Display the result in the UI
        st.divider()
        st.markdown(report)

        # Add a download button for the report
        st.download_button(
            label="📥 Download Report (.md)",
            data=report,
            file_name=f"{product_query.lower().replace(' ', '_')}_report.md",
            mime="text/markdown"
        )
    else:
        st.warning("Please enter a product name first!")