from ..component import Component


#<nav> ... </nav>
class Nav(Component):
    def __render__(self):
        return f'<nav{self.__get_attr__()}>{self.__get_children__()}</nav>'

