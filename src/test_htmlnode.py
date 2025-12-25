import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "my value", None, None)
        node2 = HTMLNode("a", "my value", None, None)
        self.assertEqual(node, node2)

    def test_not_eq_tag(self):
        node = HTMLNode("a", "my value", None, None)
        node2 = HTMLNode("p","my value", None, None)
        self.assertNotEqual(node, node2)

    def test_not_eq_value(self):
        node = HTMLNode("a", "myvalue", None, None)
        node2 = HTMLNode("a","my value", None, None)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_children(self):
        node = HTMLNode("a", "my value", HTMLNode("p","text", None, None), None)
        node2 = HTMLNode("a","my value", HTMLNode("h2","text", None, None), None)
        self.assertNotEqual(node, node2)

    def test_eq_children(self):
        child_node = HTMLNode("p","text", None, None)
        node = HTMLNode("a", "my value", child_node, None)
        node2 = HTMLNode("a","my value", child_node, None)
        self.assertEqual(node, node2)

    def test_eq_props(self):
        node = HTMLNode("a", "my value", None, {"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("a","my value", None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node, node2)

    def test_not_eq_props(self):
        node = HTMLNode("a", "my value", HTMLNode("p","text", None, None), {"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("a","my value", HTMLNode("P","text", None, None), {"href": "https://www.bing.com", "target": "_blank",})
        self.assertNotEqual(node, node2)

    def test_to_props(self):
        node = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()