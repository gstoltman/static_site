from htmlnode import HTMLNode, LeafNode
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)
        return False

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'

    def text_node_to_html_node(text_node):
        if text_node.text_type == 'text_type_text':
            html_node = LeafNode(value=text_node.text)
        elif text_node.text_type == 'text_type_bold':
            html_node = LeafNode(tag='b', value=text_node.text)
        elif text_node.text_type == 'text_type_italic':
            html_node = LeafNode(tag='i', value=text_node.text)
        elif text_node.text_type == 'text_type_code':
            html_node = LeafNode(tag='code', value=text_node.text)
        elif text_node.text_type == 'text_type_link':
            html_node = LeafNode(tag='a', value=text_node.text, props='href')
        elif text_node.text_type == 'text_type_image':
            html_node = LeafNode(tag='img', value='', props={'src': '', 'alt': ''})
        else:
            raise Exception('none of those types')
        return html_node
