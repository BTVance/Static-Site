import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com", 
             "target": "_blank",
        }
        node = HTMLNode(tag="a", value=None,children=None,props=props)
        result = node.props_to_html()
        expected =  ' href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected)
    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="hello", children=None, props={})
        result = node.props_to_html()
        expected = ""
        self.assertEqual(result, expected)
    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", value="hello", children=None, props=None)
        result = node.props_to_html()
        expected = ""
        self.assertEqual(result, expected)
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_node_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    def test_leaf_tag_none(self):
        node = LeafNode(None, "Hello")
        self.assertEqual(node.to_html(), "Hello")


if __name__ == "__main__":
    unittest.main()