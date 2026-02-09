from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    with open(markdown, "r") as f:
        for line in f:
            if line.startswith("# "):
                return line[2:].strip()
        raise ValueError("missing title")