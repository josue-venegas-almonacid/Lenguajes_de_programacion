class Component:
    def __init__(self, *children, **attr):
        """
        Constructor de cada Componente. Fija como variables
        de la clase a los hijos y a los atributos que se le pasen
        :param children: Componentes hijos
        :param attr: Atributos para el componente
        """
        self.children = children
        self.attr = attr

    def __render__(self):
        """
        Renderiza el componente y lo transforma en un tag de HTML
        :return: Componente convertido a un cadena de texto
        """
        return f'Component - childrens: {self.children} - attr: {self.attr}'

    def __repr__(self):
        return self.__render__()

    def __get_children__(self):
        """
        Obtiene todos los hijos dentro de la clase y los renderiza
        :return: Componentes hijos renderizados (cadena de texto)
        """
        children = ''
        for child in self.children:
            if issubclass(type(child), Component):
                children += child.__render__()
            else:
                children += str(child)
        return children

    def __get_attr__(self):
        """
        Obtiene los atributos a aplicar al tag HTML
        :return: Atributos del componente como cadena de texto
        """
        attributes = []
        for attribute in self.attr:
            attributes.append(f'{attribute}="{self.attr[attribute]}"')
        if len(attributes) != 0:
            return ' ' + ' '.join(attributes)
        else:
            return ''
