import smtplib

subject = 'Prueba 1 de correo desde Python'
message = 'Este es un correo enviado desde Skynet osea hackeo supremo XD'

correo = 'Subject: {}\n\n{}'.format(subject,message)

connection = smtplib.SMTP(host='smtp.gmail.com',port=587)
connection.starttls()
connection.login('creeper.lfa@gmail.com','spiderman2099')
connection.sendmail('creeper.lfa@gmail.com','francoaguilarkevindavid@gmail.com',correo)
connection.quit()

print("Correo Enviado Correctamente")