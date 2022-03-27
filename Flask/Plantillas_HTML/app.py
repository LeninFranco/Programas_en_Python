from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    titulo = "Welcome to my first Web App Baby"
    lista = ["Java", "Python", "C/C++", "JavaScript", "PHP"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/saludar")
def saludar():
    return render_template("saludo.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(port=3000,debug=True)