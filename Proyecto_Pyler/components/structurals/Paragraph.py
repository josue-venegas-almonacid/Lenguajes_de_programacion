from ..component import Component


#<p>{self.text}</p>
class Paragraph(Component):
    def __render__(self):
        return f'<p{self.__get_attr__()}>{self.__get_children__()}</p>'
