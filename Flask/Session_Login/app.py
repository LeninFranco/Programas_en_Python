from flask import Flask, session, redirect, url_for, render_template, request

app = Flask(__name__)

app.secret_key = 'mykey'

@app.route("/")
def index():
    if not "user" in session:
        return render_template("index.html")
    else:
        return redirect(url_for('home'))

@app.route("/home")
def home():
    if "user" in session:
        return render_template("home.html", user=session["user"])
    else:
        return redirect(url_for('index'))

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "adminpro":
            session["user"] = username
            return redirect(url_for('home'))
        else:
            return redirect(url_for('index'))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(port=3000,debug=True)