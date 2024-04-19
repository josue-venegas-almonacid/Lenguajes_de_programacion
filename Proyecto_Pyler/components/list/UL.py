from ..component import Component


#<li> ... </li>
class UL(Component):
    def __render__(self):
        return f'<ul{self.__get_attr__()}>{self.__get_children__()}</ul>'