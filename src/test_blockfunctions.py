import unittest

from markdown_to_blocks import markdown_to_blocks


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


if __name__ == "__main__":
    unittest.main()