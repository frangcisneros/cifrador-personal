# Importa las funciones jsonify y Blueprint desde el módulo flask
from flask import jsonify, Blueprint

# Define un blueprint llamado 'home'
home = Blueprint('home', __name__)

# Define una ruta para el endpoint '/' (raíz del sitio) dentro del blueprint 'home'
@home.route('/', methods=['GET'])
def index():
    # Crea una respuesta JSON con el contenido "OK"
    resp = jsonify("OK")
    # Establece el código de estado de la respuesta como 200 (Éxito)
    resp.status_code = 200
    # Retorna la respuesta
    return resp
