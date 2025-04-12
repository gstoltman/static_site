from textnode import TextNode
from htmlnode import HTMLNode

def main():
    new_textnode = TextNode('dummy1', 'dummy2', 'dummy3')
    print(new_textnode)

    new_htmlnode = HTMLNode(tag='p', value='Hello, world!', props={"href": "https://www.google.com","target": "_blank",})
    props_test = new_htmlnode.props_to_html()
    print(props_test)

if __name__ == "__main__":
    main()
