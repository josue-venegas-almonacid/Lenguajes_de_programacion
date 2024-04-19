from ..component import Component


#<li> ... </li>
class LI(Component):
    def __render__(self):
        return f'<li{self.__get_attr__()}>{self.__get_children__()}</li>'