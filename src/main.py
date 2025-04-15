import re
from textnode import TextNode, TextType, split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    #new_textnode = TextNode('test text', TextType.IMAGE, 'https://www.google.com')
#
    #new_htmlnode = HTMLNode(tag='p', value='Hello, world!', props={"href": "https://www.google.com","target": "_blank",})
    #props_test = new_htmlnode.props_to_html()
#
    #new_leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
#
    #text_node_to_html_node_text = text_node_to_html_node(new_textnode).to_html()
    #print(text_node_to_html_node_text)
    #node = TextNode("This is text with a `code block` word", TextType.TEXT)
    #new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
#
    #print(new_nodes)
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

    print(extract_markdown_links(text))


def text_node_to_html_node(text_node):
    if not text_node.text_type:
        return LeafNode()
    match(text_node.text_type):
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode("b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", value=text_node.text)
        case TextType.CODE:
            return LeafNode("code", value=text_node.text)
        case TextType.LINK:
            return LeafNode("a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", value=' ', props={"src": text_node.url, "alt": text_node.text}) 
        case _:
            raise Exception('wrong text type')

def extract_markdown_images(text):
    alt_text = re.findall(r'!\[(.*?)\]', text)
    url_text = re.findall(r'\((https?://[^\s)]+)\)', text)
    return list(zip(alt_text, url_text))

def extract_markdown_links(text):
    alt_text = re.findall(r'\[(.*?)\]', text)
    url_text = re.findall(r'\((https?://[^\s)]+)\)', text)
    return list(zip(alt_text, url_text))

if __name__ == "__main__":
    main()
