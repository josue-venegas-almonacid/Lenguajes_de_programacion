from .component import Component

#TITLE#
#<title>{text}</title>
class Title(Component):
    def __render__(self):
        return f'<title>{self.__get_children__()}</title>'