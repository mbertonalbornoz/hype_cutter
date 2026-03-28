import os
from smolagents import tool


@tool
def save_report_to_desktop(content: str, filename: str) -> str:
    """
    Saves the final research report as a Markdown file on the macOS Desktop.

    Args:
        content: The full markdown text of the report.
        filename: The name of the file (should end in .md).
    """
    try:
        # Automatically finds /Users/yourname/Desktop
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"✅ Success! Report saved to: {file_path}"
    except Exception as e:
        return f"❌ Error saving file: {str(e)}"