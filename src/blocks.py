from enum import Enum
from htmlnode import HTMLNode
import re

def markdown_to_blocks(markdown):
    blocks = []
    split_strings = markdown.split("\n\n")
    for string in split_strings:
        stripped_string = string.strip()
        if stripped_string == "":
            continue
        blocks.append(stripped_string)
    return blocks


class BlockType(Enum):

    HEADING = "#"
    CODE = "```"
    QUOTE = ">"
    UL = "- "
    OL = "1."
    P = "text"

def block_to_block_type(block):
    
    if re.match(r"^(#){1,6} ", block):
        return BlockType.HEADING
    if re.match(r"^`{3}.*`{3}$", block):
        return BlockType.CODE
    if re.match(r"^>", block):
        return BlockType.QUOTE
    if re.match(r"^- ", block):
        lines = block.split("\n")
        for line in lines:
            if not re.match(r"^- ", line):
                return BlockType.P
        return BlockType.UL
    if re.match(r"^1. ", block):
            lines = block.split("\n")
            i = 1
            for line in lines:
                if not re.match(rf"^{i}. ", line):
                    return BlockType.P
                i += 1
            return BlockType.OL
    return BlockType.P                

