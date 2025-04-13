class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'

    def __eq__(self, object2):
        if not isinstance(object2, HTMLNode):
            return False
        return self.tag == object2.tag and self.value == object2.value and self.children == object2.children and self.props == object2.props
    
    def to_html(self):
        raise NotImplementedError("Not implemented")
    
    # might need to strip quotes from f-string key
    def props_to_html(self):
        html = ''
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props)

    # anything to do here with inheriting from parent class?
    def to_html(self):
        props_str = ' '.join(f'{key}="{value}"' for key, value in self.props.items())
        if not self.value:
            raise ValueError('all leaf nodes must have a value')
        elif not self.tag:
            return self.value
        else:
            if props_str:
                return f'<{self.tag} {props_str}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=value, children=children, props=props)--------------------------------------
Ran 5 tests in 0.000s
        


