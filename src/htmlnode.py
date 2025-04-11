class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):

    
    def to_html(self):
        raise NotImplementedError("Not implemented")
    
    # might need to strip quotes from f-string key
    def props_to_html(self):
        props = '':
        for key, value in self.props:
            props += f" {key}={value}"
        return props


