from .component import Component

#A#
#<a> ... </a>
class A(Component):
    def __render__(self):
        return f'<a{self.__get_attr__()}>{self.__get_children__()}</a>'

#DIV#
class Div(Component):
    def __render__(self):
        return f'<div{self.__get_attr__()}>{self.__get_children__()}</div>'

#PARAGRAPH#
#<p>{self.text}</p>
class Paragraph(Component):
    def __render__(self):
        return f'<p{self.__get_attr__()}>{self.__get_children__()}</p>'

#HEADING#
#<h{size}>{text}</h{size}>
class Heading(Component):
    def __init__(self, *children, size=1, **attr):
        super().__init__(*children, **attr)
        self.size = size


    def __render__(self):
        return f'<h{self.size}{self.__get_attr__()}>{self.__get_children__()}</h{self.size}>'

#HR#
#<hr{attr}>
class HR(Component):
    def __render__(self):
        return f'<hr{self.__get_attr__()}>'

#NAV#
#<nav> ... </nav>
class Nav(Component):
    def __render__(self):
        return f'<nav{self.__get_attr__()}>{self.__get_children__()}</nav>'

#SPAN#
#<span {attr}>{text}</span>
class Span(Component):
    def __render__(self):
        return f'<span{self.__get_attr__()}>{self.__get_children__()}</span>'