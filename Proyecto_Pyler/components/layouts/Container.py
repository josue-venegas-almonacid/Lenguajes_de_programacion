from ..component import Component


class Container(Component):
    def __render__(self):
        return f'<p{self.__get_attr__()}>{self.__get_children__()}</p>'
