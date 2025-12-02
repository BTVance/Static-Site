from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
import unittest

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_delimiter_bold(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        delimiter = "`"
        text_type = TextType.CODE
        
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        
        result_nodes = split_nodes_delimiter([node], delimiter, text_type)
        
        self.assertEqual(len(result_nodes), len(expected_nodes))
        for i in range(len(result_nodes)):
            self.assertEqual(result_nodes[i], expected_nodes[i])    
    def test_invalid_markdown_delimiter(self):
        node = TextNode("This is text with a `unmatched delimiter", TextType.TEXT)
        delimiter = "`"
        text_type = TextType.CODE

        with self.assertRaises(Exception) as cm:
            split_nodes_delimiter([node], delimiter, text_type)

        self.assertEqual(str(cm.exception), "Invalid Markdown Syntax")
    
    def test_split_multiple_delimit_phrases(self):
        node = TextNode("This has `code1` and `code2` blocks.", TextType.TEXT)
        delimiter = "`"
        text_type = TextType.CODE

        expected_nodes = [
            TextNode("This has ", TextType.TEXT),
            TextNode("code1", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("code2", TextType.CODE),
            TextNode(" blocks.", TextType.TEXT),
        ]

        result_nodes = split_nodes_delimiter([node], delimiter, text_type)

        self.assertEqual(len(result_nodes), len(expected_nodes))
        for i in range(len(result_nodes)):
            self.assertEqual(result_nodes[i], expected_nodes[i])