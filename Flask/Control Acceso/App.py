from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import pymysql
from flask import *
from hashlib import md5
import smtplib 
from email.message import EmailMessage 

app = Flask(__name__)

app.secret_key = 'mykey'

temp_token = None

@app.route('/')
def index():
    if "username" in session:
        return redirect(url_for('home'))
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']
        hashPassword = md5(password.encode())
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='P0L1m4s7er!', db='crypto')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombreUsuario=%s AND passUsuario=%s", (username,hashPassword.hexdigest()))
        fila = cursor.fetchone()
        if fila == None:
            flash('danger')
            flash('Usuario o Contraseña incorrectos')
            return redirect(url_for('index'))
        else:
            session["username"] = username
            return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/home')
def home():
    if "username" in session:
        return render_template('home.html', usuario=session["username"])
    else:
        return redirect(url_for('index'))

@app.route('/crearCuenta')
def crearCuenta():
    if "username" in session:
        return redirect(url_for('home'))
    else:
        return render_template('signup.html')

@app.route('/guardarCuenta', methods=['POST'])
def guardarCuenta():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['pass']
        email = request.form['correo']
        hashPassword = md5(password.encode())
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='P0L1m4s7er!', db='crypto')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios(nombreUsuario,passUsuario,emailUsuario) VALUES(%s,%s,%s)",(username,hashPassword.hexdigest(),email))
        conn.commit()
        cursor.close()
        conn.close()
        flash('success')
        flash('Cuenta Creada Correctamente')
        return redirect(url_for('index'))

@app.route('/recuperarContrasena')
def recuperarContrasena():
    if "username" in session:
        return redirect(url_for('home'))
    else:
        return render_template('reset.html')

def getToken(userid):
    serial = Serializer('mykey',120)
    return serial.dumps({'user_id':userid}).decode('utf-8')

def verifyToken(token):
    serial = Serializer('mykey')
    try:
        user_id = serial.loads(token)['user_id']
    except: 
        return None
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='P0L1m4s7er!', db='crypto')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE idUsuario=%s", (user_id,))
    return cursor.fetchone()

def sendMail(user):
    token = getToken(user[0])
    email_subject = "Recuperación de Contraseña" 
    sender_email_address = "escomequipo1@gmail.com" 
    receiver_email_address = user[3]
    email_smtp = "smtp.gmail.com" 
    email_password = "escombros" 

    message = EmailMessage() 

    message['Subject'] = email_subject 
    message['From'] = sender_email_address 
    message['To'] = receiver_email_address 

    message.set_content(f'''Para crear una nueva contraseña, por favor de un clic al siguiente link:

    {url_for('resetPassword',token=token,_external=True)} 
    
    Si no solicitaste una recuperación de contraseña, ignora este mensaje. ''') 

    server = smtplib.SMTP(email_smtp, '587') 

    server.ehlo() 

    server.starttls() 

    server.login(sender_email_address, email_password) 

    server.send_message(message) 

    server.quit()


@app.route('/changePassword', methods=['POST'])        
def changePassword():
    if request.method == 'POST':
        email = request.form['correo']
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='P0L1m4s7er!', db='crypto')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE emailUsuario=%s", (email,))
        fila = cursor.fetchone()
        if fila == None:
            flash('danger')
            flash('No hay ningun usuario con ese correo')
            return redirect(url_for('index'))
        else:
            flash('success')
            flash('Se ha enviado un correo para la recuperación de su contraseña')
            sendMail(fila)
            return redirect(url_for('index'))

@app.route('/changePassword/<token>')
def resetPassword(token):
    global temp_token
    serial = Serializer('mykey')
    user = verifyToken(token)
    temp_token = serial.loads(token)['user_id']
    if user == None:
        flash('danger')
        flash('Se expiró la recuperación de contrasña con ese Token')
        return redirect(url_for('index'))
    else:
        return render_template('changePassword.html')

@app.route('/updatePassword', methods=['POST'])
def updatePassword():
    if request.method == 'POST':
        password = request.form['pass']
        hashPassword = md5(password.encode())
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='P0L1m4s7er!', db='crypto')
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET passUsuario=%s WHERE idUsuario=%s",(hashPassword.hexdigest(),temp_token))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=3000, debug=True)