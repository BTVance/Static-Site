import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType

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
    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "text")])
        with self.assertRaises(ValueError):
            node.to_html()
    def test_to_html_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()
    def test_to_html_many_children(self):
    # Test with several children at the same level
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold"),
            LeafNode(None, "Normal"),
            LeafNode("i", "Italic"),
            LeafNode("code", "Code"),
        ],
    )
        return node
    def test_nested_parent_nodes(self):
        inner_parent = ParentNode("span", [LeafNode("b", "bold")])
        outer_parent = ParentNode("div", [inner_parent])
        return outer_parent
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
if __name__ == "__main__":
    unittest.main()