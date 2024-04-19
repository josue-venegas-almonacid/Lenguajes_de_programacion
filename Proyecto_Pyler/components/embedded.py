from .component import Component

#AUDIO#
#<audio {attr}>{text}</audio>
class Audio(Component):
    def __render__(self):
        return f'<audio{self.__get_attr__()}>{self.__get_children__()}</audio>'

#VIDEO#
#<audio {attr}>{text}</audio>
class Video(Component):
    def __render__(self):
        return f'<video{self.__get_attr__()}>{self.__get_children__()}</video>'

#IMG#
class IMG(Component):
    def __render__(self):
        return f'<img{self.__get_attr__()}>'
