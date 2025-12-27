import unittest

from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestMultisplit(unittest.TestCase):
    def test_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [   TextNode("This is ", TextType.TEXT),
                                    TextNode("text", TextType.BOLD),
                                    TextNode(" with an ", TextType.TEXT),
                                    TextNode("italic", TextType.ITALIC),
                                    TextNode(" word and a ", TextType.TEXT),
                                    TextNode("code block", TextType.CODE),
                                    TextNode(" and an ", TextType.TEXT),
                                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                    TextNode(" and a ", TextType.TEXT),
                                    TextNode("link", TextType.LINK, "https://boot.dev"),
                                ])


# below tests from boots and copilot

    def test_plain_text(self):
        text = "just some text"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("just some text", TextType.TEXT)])

    def test_single_bold(self):
        text = "this is **bold** text"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("this is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ])

    def test_single_italic(self):
        text = "this is _italic_ text"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ])

    def test_single_code(self):
        text = "this is `code` text"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("this is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT)
        ])

    def test_single_link(self):
        text = "a [link](https://example.com)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com")
        ])

    def test_single_image(self):
        text = "![alt](https://img.com/x.png)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("alt", TextType.IMAGE, "https://img.com/x.png")
        ])

    def test_mixed_bold_italic(self):
        text = "text **bold** and _italic_"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC)
        ])

    def test_mixed_code_image_link(self):
        text = "`code` ![image](url) [link](url2)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("code", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "url"),
            TextNode(" ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url2")
        ])

    def test_multiple_bold(self):
        text = "**bold1** and **bold2**"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("bold1", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold2", TextType.BOLD)
        ])

    def test_multiple_links(self):
        text = "[a](u1) and [b](u2)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("a", TextType.LINK, "u1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("b", TextType.LINK, "u2")
        ])

    def test_adjacency_bold_italic(self):
        text = "**bold**_italic_"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("bold", TextType.BOLD),
            TextNode("italic", TextType.ITALIC)
        ])

    def test_empty_string(self):
        text = ""
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [])

    def test_only_bold(self):
        text = "**bold**"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("bold", TextType.BOLD)])

    def test_only_image(self):
        text = "![alt](url)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("alt", TextType.IMAGE, "url")])

    def test_url_correctness(self):
        text = "[link](https://boot.dev) ![img](https://imgur.com/x)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "https://imgur.com/x")
        ])


if __name__ == "__main__":
    unittest.main()