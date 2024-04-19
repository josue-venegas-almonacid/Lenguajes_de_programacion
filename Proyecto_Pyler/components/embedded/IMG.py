from ..component import Component


class IMG(Component):
    def __render__(self):
        return f'<img{self.__get_attr__()}>'
