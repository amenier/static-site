import unittest

from textnode import TextNode, TextType
from splitter import split_nodes_delimiter


class Testsplitter(unittest.TestCase):
    def test_code_mid(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("code block", TextType.CODE),
                                    TextNode(" word", TextType.TEXT),])
        
    def test_code_single(self):
        node = TextNode("`code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [TextNode("code block", TextType.CODE)])

    def test_code_end(self):
        node = TextNode("regular block `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [TextNode("regular block ", TextType.TEXT), TextNode("code block", TextType.CODE)])
    
    def test_code_start(self):
        node = TextNode("`code block` regular block", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [TextNode("code block", TextType.CODE), TextNode(" regular block", TextType.TEXT),] )

    def test_code_start_end(self):
        node = TextNode("`code block` regular block `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [TextNode("code block", TextType.CODE), TextNode(" regular block ", TextType.TEXT), TextNode("code block", TextType.CODE)] )

    def test_code_double(self):
        node = TextNode("regular block `code block` regular block `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [TextNode("regular block ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" regular block ", TextType.TEXT), TextNode("code block", TextType.CODE)] )

    def test_code_bold_italic(self):
        node = TextNode("regular block `code block` **bold block** _italic block_", TextType.TEXT)
        code_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        bold_nodes = split_nodes_delimiter(code_nodes, "**", TextType.BOLD)
        italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)

        self.assertEqual(italic_nodes, [TextNode("regular block ", TextType.TEXT), 
                                        TextNode("code block", TextType.CODE), 
                                        TextNode(" ", TextType.TEXT),
                                        TextNode("bold block", TextType.BOLD), 
                                        TextNode(" ", TextType.TEXT),
                                        TextNode("italic block", TextType.ITALIC),] )



if __name__ == "__main__":
    unittest.main()