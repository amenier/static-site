from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("odd number of delimiters")
        split_nodes = node.text.split(delimiter) #should I ignore empty strings?
        for i in range(len(split_nodes)):
            if split_nodes[i] != "":
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_nodes[i],TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_nodes[i], text_type))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\]]*)\]\(([^\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    """
    ##review each node. If it is not a text node, skip it
    ##check to see if images can be extracted.
    ##    if not, add the node to the list and continue
    ##    if so, then extract the nodes and store them in a variable
    ##        then split the string on the regex without capturing groups
            and then alternate adding nodes to new_nodes popping 0 if exists.
                if it's not an empty string
            raise errors if a link doesn't have text or a url?

    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        split_strings = re.split(r"!\[.*?\]\(.*?\)",node.text)
        num_images = len(images)
        for i in range(num_images):
            popped_string = split_strings.pop(0)
            popped_image = images.pop(0)
            if popped_string != "":
                new_nodes.append(TextNode(popped_string,TextType.TEXT))
            new_nodes.append(TextNode(popped_image[0],TextType.IMAGE,popped_image[1]))
        if split_strings[0] != "":
            new_nodes.append(TextNode(split_strings[0],TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        split_strings = re.split(r"(?<!!)\[.*?\]\(.*?\)",node.text)
        num_links = len(links)
        for i in range(num_links):
            popped_string = split_strings.pop(0)
            popped_link = links.pop(0)
            if popped_string != "":
                new_nodes.append(TextNode(popped_string,TextType.TEXT))
            new_nodes.append(TextNode(popped_link[0],TextType.LINK,popped_link[1]))
        if split_strings[0] != "":
            new_nodes.append(TextNode(split_strings[0],TextType.TEXT))

    return new_nodes