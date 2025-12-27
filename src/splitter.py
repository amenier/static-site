from textnode import TextNode, TextType

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