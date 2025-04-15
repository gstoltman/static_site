import unittest

from textnode import TextNode, TextType, split_nodes_delimiter
from main import text_node_to_html_node, extract_markdown_images

class TestTextToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

class TestDelimiterSplit(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        list1 = split_nodes_delimiter([node], '`', TextType.TEXT)
        list2 = split_nodes_delimiter([node], '`', TextType.TEXT)
        self.assertEqual(list1, list2)

    def test_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        list1 = split_nodes_delimiter([node], '`', TextType.CODE)
        list2 = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),]
        self.assertEqual(list1, list2)

class TestExtractImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()

    