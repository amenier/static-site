from textnode import TextType
from textnode import TextNode

def main():
    new_node = TextNode("Text Node", TextType.LINK_TEXT, "http://example.com")
    print(new_node)

if __name__ == "__main__":
    main()