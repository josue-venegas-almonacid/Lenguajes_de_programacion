from components.component import Component


def render(*children):
    """
    Recibe Componentes y luego los renderiza, asi se evita el tener que
    renderizar cada componente por si solo.
    :param children: Componentes a renderizar
    :return: Componentes renderizados en una cadena de texto(string)
    """
    d = ''
    for child in children:
        if issubclass(type(child), Component):
            d += child.__render__()
        else:
            d += str(child)
    return d


def display(function):
    def __render__():
        return render(function())
    return __render__


class Style:
    def __init__(self, style):
        self.style = style
        print('Creando un estilo nuevo')

    def __crear__(self):
        style = self.style
        cadena = ''
        for valor in style:
            cadena += '.' + valor +' {'
            for subvalores in style[valor]:
                cadena += subvalores+': '+style[valor][subvalores]+ '; '
            cadena += '}'
        return cadena
