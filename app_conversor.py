import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    datos = request.get_json()

    if not datos or 'valor' not in datos or 'escala' not in datos:
        return jsonify({"error": "Se requieren los campos 'valor' y 'escala'"}), 400

    valor = datos['valor']
    escala = datos['escala'].upper()

    if not isinstance(valor, (int, float)):
        return jsonify({"error": "El campo 'valor' debe ser un número"}), 400

    if escala not in ['C', 'F']:
        return jsonify({"error": "La escala debe ser 'C' (Celsius) o 'F' (Fahrenheit)"}), 400

    if escala == 'C':
        resultado = (valor * 9/5) + 32
        escala_origen = "Celsius"
        escala_destino = "Fahrenheit"
        simbolo_destino = "°F"
    else:
        resultado = (valor - 32) * 5/9
        escala_origen = "Fahrenheit"
        escala_destino = "Celsius"
        simbolo_destino = "°C"

    respuesta = {
        "valor_original": valor,
        "escala_origen": escala_origen,
        "resultado": round(resultado, 2),
        "escala_destino": escala_destino,
        "mensaje": f"{valor}° {escala_origen} equivale a {round(resultado, 2)}{simbolo_destino}"
    }

    return jsonify(respuesta), 200


if __name__ == '__main__':
    host = os.getenv('FLASK_RUN_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True') == 'True'

    app.run(host=host, port=port, debug=debug)