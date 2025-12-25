from enum import Enum

class TextType(Enum):
    BOLD = "**bold**"
    ITALIC = "_italic_"
    CODE = "`code`"
    LINK = "[link text](url)"
    IMAGE = "![alt text](image_url)"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node2):
        if self.text == node2.text \
            and self.text_type == node2.text_type \
            and self.url == node2.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

