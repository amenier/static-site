import unittest

from markdown_to_html import markdown_to_html_node


class TestMDtoHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_quoteblock(self):
        md = """
This is normal text.


>This is a quote.

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is normal text.</p><quoteblock>This is a quote.</quoteblock></div>"

        )



    def test_headings(self):
        md = """
# h1

## h2

### h3

#### h4

##### h5

###### h6


"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>h1</h1><h2>h2</h2><h3>h3</h3><h4>h4</h4><h5>h5</h5><h6>h6</h6></div>"

        )        

    def test_ul(self):
        md = """
- first unordered item
- second unordered item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>first unordered item</li><li>second unordered item</li></ul></div>"
        )        

    def test_ol(self):
        md = """
1. first item
2. second **item**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first item</li><li>second <b>item</b></li></ol></div>"
        )

    def test_multiple_blocks(self):
        md = """
# Here is some heading

This _is_ a **paragraph**

- unordered
- `list`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Here is some heading</h1><p>This <i>is</i> a <b>paragraph</b></p><ul><li>unordered</li><li><code>list</code></li></ul></div>"
        )



if __name__ == "__main__":
    unittest.main()