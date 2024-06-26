import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode('h1', 'Test text', None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode('h1', 'Test text', None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1, node2)

    def test_props_to_html(self):
        node1 = HTMLNode('h1', 'Test text', None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode('a', 'Test text', {"href": "https://www.google.com", "target": "_blank"})
        node2 = LeafNode('a', 'Test text', {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1, node2)

    def test_leaf_to_html(self):
        node1 = LeafNode('a', 'Test text', {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com" target="_blank">Test text</a>')

    def test_leaf_to_html_multi_dict(self):
        node1 = LeafNode('a', 'Test text', {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com">Test text</a>')

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node1 = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"),],)
        self.assertEqual(node1.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_parent_to_html_nested_parent(self):
        node1 = ParentNode(
            "p",
            [
                ParentNode(
                    "h1",
                    [
                        LeafNode("b", "Bold text 2"),
                        LeafNode("i", "Italic text 2")
                    ],
                ),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node1.to_html(), '<p><h1><b>Bold text 2</b><i>Italic text 2</i></h1><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

if __name__ == "__main__":
    unittest.main()