import unittest

from blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMDtoBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_md(self):
        md = """

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks, [],
        )

    def test_extra_spaces_md(self):
        md = """
This is text





There were extra blank spaces there
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks, ["This is text", "There were extra blank spaces there"],
        )


    def test_needs_trimming_md(self):
        md = """
This is text that needs to be trimmed               

    # This heading has leading spaces
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks, ["This is text that needs to be trimmed", "# This heading has leading spaces"],
        )

    # Below tests from Boots

    def test_whitespace_only_blocks_removed(self):
        md = "First\n\n   \n\t\nSecond"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First", "Second"])

    def test_trailing_newline(self):
        md = "First block\n\nSecond block\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block"])

    def test_single_block_no_newlines(self):
        md = "Just a single line of text"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just a single line of text"])

    def test_paragraph_with_internal_newlines(self):
        md = """First line
Second line

Next block"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
        blocks,
        ["First line\nSecond line", "Next block"],
        )


class TestBlockTypeCheckerHEADING(unittest.TestCase):
    def test_heading_1(self):
        block = "# Heading1"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_2(self):
        block = "## Heading2"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_3(self):
        block = "### Heading3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_4(self):
        block = "#### Heading4"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_5(self):
        block = "##### Heading5"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_6(self):
        block = "###### Heading6"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)
    
    def test_fake_heading(self):
        block = "######Heading6"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)
    
    def test_mid_fake_heading(self):
        block = "Other text ###### Heading6"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)

    def test_mid_fake_seven_heading(self):
        block = "####### Heading6"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)

class TestBlockTypeCheckerCODE(unittest.TestCase):
    def test_code(self):
        block = "```code block```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_code_multiline(self):
        block = "```\ncode \n\n\nblock\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_mid_fake_code(self):
        block = "Other text ```code``` other text"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)

    def test_start_fake_code(self):
        block = "```code``` other text"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)
    
    def test_end_fake_code(self):
        block = "Other text ```code```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)

class TestBlockTypeCheckerQUOTE(unittest.TestCase):
    def test_quote(self):
        block = ">quote"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_mid_fake_quote(self):
        block = "Other text >quote other text"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)
    
    def test_end_fake_quote(self):
        block = "Other text >quote"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)

    def test_double_quote(self):
        block = ">quote >quote"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

class TestBlockTypeCheckerUL(unittest.TestCase):
    def test_single_UL(self):
        block = """- single ul"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UL)

    def test_double_UL(self):
        block = """- single ul\n- second line"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UL)

    def test_triple_UL(self):
        block = """- single ul\n- second line\n- third line"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UL)

    def test_fake_UL_nospace_first(self):
        block = """-single ul\n- second line\n- third line"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)

    def test_fake_UL_nospace_second(self):
        block = """-single ul\nsecond line\n- third line"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)

class TestBlockTypeCheckerOL(unittest.TestCase):
    def test_single_OL(self):
        block = """1. single ul"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.OL)

    def test_double_OL(self):
        block = """1. single ul\2. second line"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.OL)

    def test_triple_OL(self):
        block = """1. single ul\n2. second line\n3. third line"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.OL)

    def test_fake_OL_nospace_first(self):
        block = """1.single ul\n2. second line\n3. third line"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)

    def test_fake_OL_nospace_second(self):
        block = """1. single ul\n2.second line\n-=3. third line"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)

    def test_fake_OL_disordered(self):
        block = """1. single ul\n2. second line\n-3. third line\n7. other"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.P)

if __name__ == "__main__":
    unittest.main()