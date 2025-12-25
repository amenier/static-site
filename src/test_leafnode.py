import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "my value", None)
        node2 = LeafNode("a", "my value", None)
        self.assertEqual(node, node2)

    def test_not_eq_tag(self):
        node = LeafNode("a", "my value", None)
        node2 = LeafNode("p","my value", None)
        self.assertNotEqual(node, node2)

    def test_not_eq_value(self):
        node = LeafNode("a", "myvalue", None)
        node2 = LeafNode("a","my value", None)
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Hello, world!",{"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Hello, world!</a>')

    def test_no_tag(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_value_error_no_text(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode("a", None)
            node.to_html()

            self.assertIn(str(context.exception), "leaf nodes must have a value")

if __name__ == "__main__":
    unittest.main()