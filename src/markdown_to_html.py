from blocks import BlockType, markdown_to_blocks, block_to_block_type
from parentnode import ParentNode
from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    leaf_nodes = []
    for node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(node))
    #print("leaf nodes are", leaf_nodes)
    return leaf_nodes


def p_block_to_node(p_block):
    lines = p_block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def code_block_to_node(code_block):
    code = code_block.strip("`")
    if code.startswith("\n"):
        code = code[1:]
    code_text_node = text_node_to_html_node(TextNode(code,TextType.TEXT))
    return ParentNode("pre", [ParentNode("code",[code_text_node])])

def quote_block_to_node(quote_block):
    quote_text = quote_block[1:]
    children = text_to_children(quote_text)
    return ParentNode("quoteblock", children)

def heading_block_to_node(heading_block):
    hash_count = 0
    while heading_block[hash_count] == "#":
        hash_count += 1
    heading_text = heading_block.strip("#").strip()
    children = text_to_children(heading_text)
    return ParentNode(f"h{hash_count}", children)



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    ##root_node = ParentNode("html",[ParentNode("body",["body child"],None)], None)
    ##print(root_node.children[0].children)
    node_list = []
    for block in blocks:
        print("BLOCK RAW:", repr(block), "TYPE:", block_to_block_type(block))  # TEMP
        block_type = block_to_block_type(block)
        #print(block_type)
        #print(block)
        if block_type == BlockType.CODE:
            node_list.append(code_block_to_node(block))
        elif block_type == BlockType.P:
            node_list.append(p_block_to_node(block))
        elif block_type == BlockType.QUOTE:
            node_list.append(quote_block_to_node(block))
        elif block_type == BlockType.HEADING:
            node_list.append(heading_block_to_node(block))
    return ParentNode("div", node_list)
    #turn the blocks into parent nodes
    # each block type will have a helper function


#markdown_to_html_node("some markdown")
#print(markdown_to_html_node("```                 code node```").to_html())




    