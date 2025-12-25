import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        child_node = LeafNode("p","text", None)
        node = ParentNode("a", [child_node], None)
        node2 = ParentNode("a", [child_node], None)
        self.assertEqual(node, node2)

    def test_not_eq_diff_children(self):
        child_node = LeafNode("p","text", None)
        child_node2 = LeafNode("a","text", None)
        node = ParentNode("p", [child_node], None)
        node2 = ParentNode("p",[child_node2], None)
        self.assertNotEqual(node, node2)

    def test_not_eq_props(self):
        child_node = LeafNode("p","text", None)
        node = ParentNode("a", [child_node], {"href": "example.com"})
        node2 = ParentNode("a",[child_node], {"href": "no.com"})
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = ParentNode("div", [LeafNode("p","text", None)])
        self.assertEqual(node.to_html(), "<div><p>text</p></div>")

    def test_leaf_to_html_with_props(self):
        node = ParentNode("div",[LeafNode("a", "Hello, world!",{"href": "https://example.com"})])
        self.assertEqual(node.to_html(), '<div><a href="https://example.com">Hello, world!</a></div>')

    def test_value_error_no_tag(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode(None, [LeafNode("p","text", None)])
            node.to_html()

            self.assertIn(str(context.exception), "parent nodes must have a tag")

    def test_value_error_no_children(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode("a", None)
            node.to_html()

            self.assertIn(str(context.exception), "parent nodes must have children")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_raw_text(self):
        node = ParentNode("p",
        [   LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

if __name__ == "__main__":
    unittest.main()