# Pyler
La biblioteca para construir UI’s

Basado en Flask y Bootstrap, Pyler es un framework que permite al usuario crear su propio sitio web de manera declarativa y rápida.
## Primeros pasos
### Instalación
<pre>
pip install pyler
</pre>
### Hello World
```python
import Pyler
from components import Heading

@Pyler.display
def hello_world():
  return Heading('Hola Mundo')
```
## Equipo
- @therialguz
- @BrannDestroyer
- @st4rb00y

## Licencia
