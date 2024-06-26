class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
        return False

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html_string = ''
        for key, value in self.props.items():
            html_string += f' {key}="{value}"'
        return html_string

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode requires a value.")
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.tag:
            return self.value
        elif not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            props_html = self.props_to_html()
            return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag is None:
            raise ValueError("ParentNode requires a tag.")
        elif children is None:
            raise ValueError("ParentNode requires a child.")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        html_string = f'<{self.tag}>'
        for child in self.children:
            html_string += child.to_html()
        html_string += f'</{self.tag}>'
        return html_string