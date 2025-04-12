import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is an HTML node")
        node2 = HTMLNode("This is an HTML node")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("This is an HTML node")
        node2 = HTMLNode("This is a different HTML node")
        self.assertNotEqual(node, node2)

    def test_print(self):
        expected_print = "HTMLNode(tag=p, value=Hello, world!, children=None, props={'class': 'text'})"
        actual_print = HTMLNode(tag='p', value='Hello, world!', props={'class': 'text'})
        self.assertEqual(expected_print, repr(actual_print))

    def test_tag_none(self):
        node = HTMLNode(tag=None)
        self.assertIsNone(node.tag)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        node_to_html = node.props_to_html()
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected_result, node_to_html)


if __name__ == "__main__":
    unittest.main()
