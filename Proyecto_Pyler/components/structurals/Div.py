from ..component import Component


class Div(Component):
    def __render__(self):
        return f'<div{self.__get_attr__()}>{self.__get_children__()}</div>'
