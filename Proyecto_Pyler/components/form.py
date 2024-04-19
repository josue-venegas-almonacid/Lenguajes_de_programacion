from .component import Component

#BUTTON#
#<button {attributes}>{text}</button>
class Button(Component):
    def __render__(self):
        return f'<button{self.__get_attr__()}>{self.__get_children__()}</button>'
