from enum import Enum
from htmlnode import HTMLNode
import re

print("USING markdown_blocks FROM:", __file__) # debug


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
    #print("MY B2BT CALLED WITH:", repr(block[:20])) #debug
    lines = block.split("\n") 
    #print("MY B2BT LINES:", [repr(l) for l in lines]) #debug

    if re.match(r"^(#){1,6} ", block):
        return BlockType.HEADING
    if re.match(r"^`{3}.*`{3}$", block): # Code detection could use more work on edges and formats
        return BlockType.CODE
    #if len(lines) > 1 and re.match(r"^`{3}", lines[0]) and re.match(r"`{3}", lines[-1]):
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if re.match(r"^>", block):
        return BlockType.QUOTE
    if re.match(r"^- ", block):
        for line in lines:
            if not re.match(r"^- ", line):
                return BlockType.P
        return BlockType.UL
    if re.match(r"^1. ", block):
            i = 1
            for line in lines:
                if not re.match(rf"^{i}. ", line):
                    return BlockType.P
                i += 1
            return BlockType.OL
    return BlockType.P                

