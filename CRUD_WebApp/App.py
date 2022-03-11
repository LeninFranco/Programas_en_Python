from flask import *
import sqlite3

#Creacion del servidor
app = Flask(__name__)

#Sesiones para mensajes Flash
app.secret_key = 'mykey'

#Ruta y metodo de la ruta de inicio
@app.route('/') #Ruta Home o Index
def home():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.execute("SELECT * FROM Users")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", users = rows) #Retorna el html index y pasamos datos al HTML para usarlos

#Ruta y metodo para añadir un usuario
@app.route('/add_user', methods=['POST']) #Ruta del add_user y usa POST como HTTPRequest 
def add():
    if request.method == 'POST':
        userid = request.form['idUser'] #Obtenemos el valor de un input del formulario
        username = request.form['username'] #Obtenemos el valor de un input del formulario
        password = request.form['password'] #Obtenemos el valor de un input del formulario
        conn = sqlite3.connect("usuarios.db")
        conn.execute('''INSERT INTO Users(IdUser,Name,Password) VALUES(?,?,?)''',(int(userid),username,password))
        conn.commit()
        conn.close()
        flash('User Added Successfully') #Envia mensaje por flash para recuperarla en el HTML
        return redirect(url_for('home')) #Reedirige al Index. Dentro de url_for debe ser el nombre de la funcion asociada a la ruta

@app.route('/delete/<string:id>') #ruta del delete pero con un parametro de tipo string que es un ID
def delete(id):
    conn = sqlite3.connect("usuarios.db")
    conn.execute('''DELETE FROM Users WHERE IdUser = ?''',(int(id),))
    conn.commit()
    conn.close()
    flash('User Deleted Successfully') #Envia mensaje por flash para recuperarla en el HTML
    return redirect(url_for('home')) #Reedirige al Index. Dentro de url_for debe ser el nombre de la funcion asociada a la ruta

@app.route("/edit/<string:id>") #ruta del delete pero con un parametro de tipo string que es un ID
def edit(id):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.execute('''SELECT * FROM Users WHERE IdUser = ?''',(int(id),))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit.html', user = row) #Retorna el html index y pasamos datos al HTML para usarlos

@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        userid = request.form['idUser'] #Obtenemos el valor de un input del formulario
        username = request.form['username'] #Obtenemos el valor de un input del formulario
        password = request.form['password'] #Obtenemos el valor de un input del formulario
        conn = sqlite3.connect("usuarios.db")
        conn.execute('''UPDATE Users SET Name=?, Password=? WHERE IdUser=?''',(username,password,int(userid)))
        conn.commit()
        conn.close()
        flash('User Updated Successfully') #Envia mensaje por flash para recuperarla en el HTML
        return redirect(url_for('home')) #Reedirige al Index. Dentro de url_for debe ser el nombre de la funcion asociada a la ruta

if __name__ == "__main__":
    app.run(port=3000, debug=True)