class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        prop_list = []
        for prop in self.props:
            prop_list.append(f'{prop}="{self.props[prop]}"')
        return ' ' + ' '.join(prop_list)
    
    def __eq__(self, node2):
        if self.tag == node2.tag \
        and self.value == node2.value \
        and self.children == node2.children \
        and self.props == node2.props:
            return True
        return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

