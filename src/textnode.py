from enum import Enum

class TextType(Enum):
    BOLD_TEXT = "**bold**"
    ITALIC_TEXT = "_italic_"
    CODE_TEXT = "`code`"
    LINK_TEXT = "[link text](url)"
    IMAGE_TEXT = "![alt text](image_url)"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node1, node2):
        if node1.text == node2.text \
            and node1.text_type == node2.text_type \
            and node1.url == node2.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

