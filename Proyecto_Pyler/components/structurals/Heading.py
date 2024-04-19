from ..component import Component


#<h{size}>{text}</h{size}>
class Heading(Component):
    def __init__(self, *children, size=1, **attr):
        super().__init__(*children, **attr)
        self.size = size


    def __render__(self):
        return f'<h{self.size}{self.__get_attr__()}>{self.__get_children__()}</h{self.size}>'
