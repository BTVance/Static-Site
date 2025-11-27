class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  
        self.value = value
        self.children = children or []
        self.props = props or {}
    def to_html(self):
        raise [NotImplementedError]
    def props_to_html(self):
        if not self.props:
            return ""
        else:
            string = ""
            for key, value in self.props.items():
                string += f' {key}="{value}"'
            return string
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None,props=props)
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag is None:
            return self.value
        else:
           attrs = None
           if self.props is None:
                attrs = ""
           else:
                attrs = ""
                for key, value in self.props.items():
                    attrs += f' {key}="{value}"'
        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"
