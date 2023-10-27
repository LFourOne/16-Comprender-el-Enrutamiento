from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola Mundo!"

@app.route("/dojo")
def dojo():
    return "¡Dojo!"

@app.route("/say/<string:thing>")
def thing(thing):
    return f"¡Hola, {thing}!"

@app.route("/repeat/<int:numero>/<string:anything>")
def numanything(numero, anything):
    return anything * numero

@app.route("/<path:nothing>")
def nothing(nothing):
    return "Lo siento! No hay respuesta. Inténtalo otra vez."

if __name__=="__main__":
    app.run(debug=True)