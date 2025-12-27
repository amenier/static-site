import unittest

from textnode import TextNode, TextType
from inline import split_nodes_image, split_nodes_link


class TestImageLinkSplitter(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),],new_nodes,)

    def test_split_image_start(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),],new_nodes,)


    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/) and another [link](https://example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "link", TextType.LINK, "https://example.com"
                ),],new_nodes,)
        
    def test_split_link_not_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/example.png) and another [link](https://example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("This is text with an ![image](https://i.imgur.com/example.png) and another ", TextType.TEXT),
                TextNode(
                    "link", TextType.LINK, "https://example.com"
                ),],new_nodes,)

    def test_split_link_only_text(self):
        node = TextNode("This only has text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("This only has text", TextType.TEXT)], new_nodes)

    def test_split_link_only_link(self):
        node = TextNode("[This only has link text](/example)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("This only has link text", TextType.LINK, "/example")], new_nodes)

    def test_split_link_adjacent_links(self):
        node = TextNode("[one](a)[two](b)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("one", TextType.LINK, "a"),TextNode("two", TextType.LINK, "b"),], new_nodes)

    def test_split_image_not_link(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/example.png) and another [link](https://example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/example.png"),
                TextNode(" and another [link](https://example.com)", TextType.TEXT),], new_nodes)


    def test_split_image_and_link(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/example.png) and another [link](https://example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        next_nodes = split_nodes_link(new_nodes)
        self.assertListEqual(
            [TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/example.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "link", TextType.LINK, "https://example.com"
                ),], next_nodes)
        
    
    def test_split_image_only_text(self):
        node = TextNode("This only has text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("This only has text", TextType.TEXT)], new_nodes)

    def test_split_image_only_image(self):
        node = TextNode("![This only has image text](/example.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("This only has image text", TextType.IMAGE, "/example.png")], new_nodes)

    def test_split_image_adjacent_images(self):
        node = TextNode("![one](a)![two](b)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("one", TextType.IMAGE, "a"),TextNode("two", TextType.IMAGE, "b"),], new_nodes)


if __name__ == "__main__":
    unittest.main()