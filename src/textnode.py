from enum import Enum

# UNSURE ABOUT BELOW CLASS
class TextType(Enum):
    NORMAL = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, object2):
        if self == object2:
            return True
    
    # MIGHT NEED .value on text_type
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

