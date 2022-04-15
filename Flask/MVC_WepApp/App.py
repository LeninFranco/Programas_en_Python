from flask import *
from Modelo import Producto
from DAO import ProductoDAO

app = Flask(__name__)

app.secret_key = 'mykey'

@app.route('/')
def home():
    dao = ProductoDAO()
    lista = dao.selectAll()
    return render_template('index.html', productos = lista)

@app.route('/add', methods=['POST'])
def add():
    if request.method == "POST":
        ID = request.form['idProduct']
        nombre = request.form['nombre']
        precio = request.form['precio']
        p = Producto(ID, nombre, float(precio))
        dao = ProductoDAO()
        dao.create(p)
        flash('success')
        flash('Producto Añadido Correctamente')
        return redirect(url_for('home'))

@app.route('/edit/<string:id>')
def edit(id):
    dao = ProductoDAO()
    p = dao.selectOne(Producto(id,"",0.0))
    return render_template('edit.html', producto = p)

@app.route('/update', methods=['POST'])
def update():
    if request.method == "POST":
        ID = request.form['idProduct']
        nombre = request.form['nombre']
        precio = request.form['precio']
        p = Producto(ID, nombre, float(precio))
        dao = ProductoDAO()
        dao.update(p)
        flash('success')
        flash('Producto Actualizado Correctamente')
        return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    dao = ProductoDAO()
    p = dao.delete(Producto(id,"",0.0))
    flash('danger')
    flash('Producto Eliminado Correctamente')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(port=3000, debug=True)