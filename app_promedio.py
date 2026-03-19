import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    datos = request.get_json()

    if not datos or 'nombre' not in datos or 'calificaciones' not in datos:
        return jsonify({"error": "Se requieren los campos 'nombre' y 'calificaciones'"}), 400

    nombre = datos['nombre']
    calificaciones = datos['calificaciones']

    if not calificaciones or len(calificaciones) == 0:
        return jsonify({"error": "La lista de calificaciones no puede estar vacía"}), 400

    promedio = sum(calificaciones) / len(calificaciones)

    respuesta = {
        "nombre": nombre,
        "calificaciones": calificaciones,
        "promedio": round(promedio, 2)
    }

    return jsonify(respuesta), 200


if __name__ == '__main__':
    host = os.getenv('FLASK_RUN_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True') == 'True'

    app.run(host=host, port=port, debug=debug)