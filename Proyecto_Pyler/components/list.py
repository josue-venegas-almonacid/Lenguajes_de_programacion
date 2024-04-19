from .component import Component

#LI#
#<li> ... </li>
class LI(Component):
    def __render__(self):
        return f'<li{self.__get_attr__()}>{self.__get_children__()}</li>'

#UL#
#<ul> ... </ul>
class UL(Component):
    def __render__(self):
        return f'<ul{self.__get_attr__()}>{self.__get_children__()}</ul>'