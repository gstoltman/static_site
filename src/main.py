from textnode import TextNode

if __name__ == "__main__":
    textnode1 = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    textnode2 = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    textnode3 = TextNode('This is a text node', 'italic', 'https://www.boot.dev')

    print(textnode1)
    print(textnode2)
    print(textnode3)

    print(textnode1 == textnode2)
    print(textnode1 == textnode3)