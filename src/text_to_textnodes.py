from textnode import TextNode, TextType
from inline import split_nodes_image, split_nodes_delimiter, split_nodes_link

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    image_nodes = split_nodes_image([node])
    link_nodes = split_nodes_link(image_nodes)
    code_nodes = split_nodes_delimiter(link_nodes, "`", TextType.CODE)
    bold_nodes = split_nodes_delimiter(code_nodes, "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)

    return italic_nodes