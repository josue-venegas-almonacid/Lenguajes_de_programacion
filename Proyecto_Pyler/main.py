# PASO 1: Definir renders de cada elemento de HTML importante:
#Structural
#List
#Embedded Content Tags: few of them
#Form tags: few
# https://www.tutorialrepublic.com/html-reference/html5-tags.php
# PASO 2: Personalizaciones de texto (color, tamaño) y creaciones de plantillas

import Pyler
from flask import Flask
from components import Heading, Paragraph, Div, HR, IMG, Nav, LI, UL, A
app = Flask(__name__)
'''<nav>
    <ul>
        <li> <a  href = "#"> Inicio </a> </ li>
        <li> <a  href = "#"> Acerca </a> </ li>
        <li> <a  href = "#"> Contacto </a> </ li>
    </ul>
</nav>'''


@app.route("/")
@Pyler.display
def index():
    return Div(
            Heading("Buena cabros!", size=1, style="color:red;text-align:center;"),
            HR(),
            Paragraph("Acabamos de crear nuestra propia pagina web!!!", style="color:blue;text-align:center;"),
            Nav(
                UL(
                    LI(
                        A("INICIO", href = "https://www.xnxx.com/video-u21ntc7/nayafacil_facil"),
                        HR()
                    ),
                    LI(
                        A("ACERCA DE", href = "https://www.youtube.com/watch?v=3v79CLLhoyE")
                    )
                )
            ),
            HR(),
            #IMG(src="https://instagram.fscl11-2.fna.fbcdn.net/v/t51.2885-15/e15/1171042_603834193022882_1352707368_n.jpg?_nc_ht=instagram.fscl11-2.fna.fbcdn.net&_nc_cat=102&_nc_ohc=hW5SGhVQqOIAX_eimvY&oh=309c20d7ec86f6a492ff414d43025032&oe=5EB37789", alt="Josue siendo josue"),
            style="background-image: url(https://instagram.fscl11-2.fna.fbcdn.net/v/t51.2885-15/e15/1171042_603834193022882_1352707368_n.jpg?_nc_ht=instagram.fscl11-2.fna.fbcdn.net&_nc_cat=102&_nc_ohc=hW5SGhVQqOIAX_eimvY&oh=309c20d7ec86f6a492ff414d43025032&oe=5EB37789); height:864px; width:1536px",
        )


if __name__ == "__main__":
    print('Pyler is running as program')
    app.run(debug=True)
