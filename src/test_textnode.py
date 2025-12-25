import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("First Node", TextType.BOLD)
        node2 = TextNode("Second node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("Node", TextType.BOLD)
        node2 = TextNode("Node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_link_has_url(self):
        node = TextNode("Link Text",TextType.LINK, "https://example.com")
        self.assertNotEqual(node.url, None)



if __name__ == "__main__":
    unittest.main()