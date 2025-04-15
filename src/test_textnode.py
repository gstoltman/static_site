import unittest

from textnode import TextNode, TextType, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("Test node", TextType.BOLD)
        node2 = TextNode("Test node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("Test node", TextType.LINK)
        self.assertIsNone(node.url)

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

if __name__ == "__main__":
    unittest.main()
