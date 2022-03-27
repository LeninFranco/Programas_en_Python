from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome"

@app.route("/Saludo")
def Saludo():
    return "Hello My Friend :3"

@app.route("/nombre/<string:name>")
def nombre(name):
    return "Your username is " + name + " :)"

@app.route("/edad/<int:age>")
def edad(age):
    return f"You are {age} years old :)"

@app.route("/user/<int:id>/<string:username>")
def register(id,username):
    return f"You are {username} and your ID is {id}"

@app.route("/default/")
@app.route("/default/<string:text>")
def printText(text="Hola Mundo"):
    return f"Your Text is: {text}"

if __name__ == "__main__":
    app.run(port=3000,debug=True)