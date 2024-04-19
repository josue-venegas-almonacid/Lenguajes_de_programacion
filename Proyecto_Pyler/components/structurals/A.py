from ..component import Component


#<a> ... </a>
class A(Component):
    def __render__(self):
        return f'<a{self.__get_attr__()}>{self.__get_children__()}</a>'