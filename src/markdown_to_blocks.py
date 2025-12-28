from htmlnode import HTMLNode

def markdown_to_blocks(markdown):
    blocks = []
    split_strings = markdown.split("\n\n")
    for string in split_strings:
        stripped_string = string.strip()
        if stripped_string == "":
            continue
        blocks.append(stripped_string)
    return blocks


