from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    for line in block:
        if re.match(r"^#{1,6}\s", line):
            return BlockType.HEADING
        elif line.startswith('```'):
            return BlockType.CODE
        elif line.startswith('>'):
            return BlockType.QUOTE
        elif line.startswith('-'):
            return BlockType.UNORDERED_LIST
        elif line.re.match(r"^[a-zA-Z0-9]\.", line):
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
