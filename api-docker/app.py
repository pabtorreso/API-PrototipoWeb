from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para toda la aplicación

@app.route('/')
def ping():
    data = {
        "code": 200,
        "response": "Respuesta desde API en Docker"
    }
    return jsonify(data)

@app.route('/medicos')
def medicos():
    data = {
        "code": 200,
        "medicos": [
            {
                "id": 1,
                "name": "Dr. Juan Pérez",
                "available": True,
                "img": "https://example.com/medico1.jpg",
                "especialidad": "Cardiología"
            },
            {
                "id": 2,
                "name": "Dra. María González",
                "available": False,
                "img": "https://example.com/medico2.jpg",
                "especialidad": "Neurología"
            },
            {
                "id": 3,
                "name": "Dr. Roberto Díaz",
                "available": True,
                "img": "https://example.com/medico3.jpg",
                "especialidad": "Pediatría"
            },
            {
                "id": 4,
                "name": "Dra. Carmen Ruiz",
                "available": False,
                "img": "https://example.com/medico4.jpg",
                "especialidad": "Dermatología"
            },
            {
                "id": 5,
                "name": "Dr. Antonio Ramírez",
                "available": True,
                "img": "https://example.com/medico5.jpg",
                "especialidad": "Ortopedia"
            }
        ]
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
