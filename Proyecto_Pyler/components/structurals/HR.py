from ..component import Component


#<hr{attr}>
class HR(Component):
    def __render__(self):
        return f'<hr{self.__get_attr__()}>'
