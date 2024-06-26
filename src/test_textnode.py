import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", "bold", "http://example.com")
        self.assertIsNotNone(node.url, "The url property should not be None")
        self.assertEqual(node.url, "http://example.com")

    def test_text_type(self):
        node1 = TextNode("This is a text node", "bold", "http://example.com")
        node2 = TextNode("This is a text node", "italic", "http://example.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()