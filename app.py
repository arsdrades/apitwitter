from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})


from usuarios import usuarios

@app.route('/ping')
def ping():
    return jsonify({"message" : "pong"})


@app.route('/usuarios')
def getusuarios():
    return jsonify(usuarios)

@app.route('/usuarios/<string:usuario_name>')
def getUsuario(usuario_name):
    usuariosFound = [usuario for usuario in usuarios if usuario['name'] == usuario_name]
    if (len(usuariosFound) > 0):
        return jsonify({"usuario": usuariosFound[0]})
    return jsonify({"message": "Usuario No encontrado"})




if __name__ == '__main__':
    app.run(debug=True, port=4000)