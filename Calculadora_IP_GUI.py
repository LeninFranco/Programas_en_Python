#Instalar el siguiente paquete
#1. pip install ipaddress

from tkinter import *
import tkinter.scrolledtext
import ipaddress
import re

def isNumber(char):
    return char in "0123456789."

regex = re.compile(r'([0-9]+).([0-9]+).([0-9]+).([0-9]+)') #Expresion regular para separar cada octeto del IP

netmask_class_a = {
    'A': '/8',
    'B': '/16',
    'C': '/24'
}

netmask_class_f = {
    'A': '255.0.0.0',
    'B': '255.255.0.0',
    'C': '255.255.255.0'
}

def clasificarIP(IP):
    IP_list = list(re.findall(regex,IP)[0]) #Guardamos los octetos de la direccion IP en una lista
    IP_binary_string = '.'.join(bin(int(i))[2:].zfill(8) for i in IP_list) #Convertimos cada octeto en binario
    if IP_binary_string.startswith('0'):
        return 'A'
    if IP_binary_string.startswith('10'):
        return 'B'
    elif IP_binary_string.startswith('110'):
        return 'C'

def findBitHost(var):
    n = 1
    while True:
        if (2**n)-2 >= var:
            return n
        n += 1

def findBitSubNet(var):
    n = 1
    while True:
        if (2**n) >= var:
            return n
        n += 1

def usandoHost(IP,hosts):
    clase = clasificarIP(IP)
    if clase == 'A':
        bitsHost = findBitHost(hosts)
        bitsSubnet = 24 - bitsHost
        prefijo = bitsSubnet + 8
        return (bitsHost, bitsSubnet, prefijo)
    if clase == 'B':
        bitsHost = findBitHost(hosts)
        bitsSubnet = 16 - bitsHost
        prefijo = bitsSubnet + 16
        return (bitsHost, bitsSubnet, prefijo)
    if clase == 'C':
        bitsHost = findBitHost(hosts)
        bitsSubnet = 8 - bitsHost
        prefijo = bitsSubnet + 24
        return (bitsHost, bitsSubnet, prefijo)

def usandoSubred(IP,subredes):
    clase = clasificarIP(IP)
    if clase == 'A':
        bitsSubnet = findBitSubNet(subredes)
        bitsHost = 24 - bitsSubnet
        prefijo = bitsSubnet + 8
        return (bitsHost, bitsSubnet, prefijo)
    if clase == 'B':
        bitsSubnet = findBitSubNet(subredes)
        bitsHost = 16 - bitsSubnet
        prefijo = bitsSubnet + 16
        return (bitsHost, bitsSubnet, prefijo)
    if clase == 'C':
        bitsSubnet = findBitSubNet(subredes)
        bitsHost = 8 - bitsSubnet
        prefijo = bitsSubnet + 24
        return (bitsHost, bitsSubnet, prefijo)

def printOneSubred(subred):
    hostsL = list(ipaddress.ip_network(subred).hosts())
    for host in hostsL:
        hosts.insert('end', str(host) + "\n")
    hosts.insert('end', "\nBroadcast: " + str(subred.broadcast_address))

def porHost():
    ip = eIP.get()
    numhost = int(eVal.get())
    clase = clasificarIP(ip)
    datos = usandoHost(ip,numhost)
    ip += netmask_class_a[clasificarIP(ip)]
    subredesL = list(ipaddress.ip_network(ip).subnets(new_prefix=datos[2]))
    lbClase.set(lbClase.get() + " " + str(clase))
    lbMaskP.set(lbMaskP.get() + " " + str(netmask_class_f[clase]))
    lbSubredes.set(lbSubredes.get() + " " + str(2**datos[1]))
    lbHosts.set(lbHosts.get() + " " + str(2**datos[0] - 2))
    lbMask.set(lbMask.get() + " " + str(subredesL[0].netmask))
    subredes.insert('end', "Lista de Subredes\n")
    for subred in subredesL:
        subredes.insert('end', str(subred) + "\n")
    hosts.insert('end', "Hosts de la primera subred\n")
    printOneSubred(subredesL[1])


def porSubred():
    ip = eIP.get()
    numsubs = int(eVal.get())
    clase = clasificarIP(ip)
    datos = usandoSubred(ip,numsubs)
    ip += netmask_class_a[clasificarIP(ip)]
    subredesL = list(ipaddress.ip_network(ip).subnets(new_prefix=datos[2]))
    lbClase.set(lbClase.get() + " " + str(clase))
    lbMaskP.set(lbMaskP.get() + " " + str(netmask_class_f[clase]))
    lbSubredes.set(lbSubredes.get() + " " + str(2**datos[1]))
    lbHosts.set(lbHosts.get() + " " + str(2**datos[0] - 2))
    lbMask.set(lbMask.get() + " " + str(subredesL[0].netmask))
    subredes.insert('end', "Lista de Subredes\n")
    for subred in subredesL:
        subredes.insert('end', str(subred) + "\n")
    hosts.insert('end', "Hosts de la primera subred\n")
    printOneSubred(subredesL[1])

def porPrefijo():
    ip = eIP.get()
    prefijo = int(eVal.get())
    clase = clasificarIP(ip)
    ip += netmask_class_a[clasificarIP(ip)]
    subredesL = list(ipaddress.ip_network(ip).subnets(new_prefix=prefijo))
    datos = usandoSubred(ip,len(subredesL))
    lbClase.set(lbClase.get() + " " + str(clase))
    lbMaskP.set(lbMaskP.get() + " " + str(netmask_class_f[clase]))
    lbSubredes.set(lbSubredes.get() + " " + str(len(subredesL)))
    lbHosts.set(lbHosts.get() + " " + str(2**datos[0] - 2))
    lbMask.set(lbMask.get() + " " + str(subredesL[0].netmask))
    subredes.insert('end', "Lista de Subredes\n")
    for subred in subredesL:
        subredes.insert('end', str(subred) + "\n")
    print("Hosts de la primera subred\n")
    hosts.insert('end', "Hosts de la primera subred\n")
    printOneSubred(subredesL[1])

def datos():
    opc = variableRadio.get()
    if opc == 1:
        ip = eIP.get()
        numhost = int(eVal.get())
        clase = clasificarIP(ip)
        datos = usandoHost(ip,numhost)
        ip += netmask_class_a[clasificarIP(ip)]
        subredesL = list(ipaddress.ip_network(ip).subnets(new_prefix=datos[2]))
        lbClase.set(lbClase.get() + " " + str(clase))
        lbMaskP.set(lbMaskP.get() + " " + str(netmask_class_f[clase]))
        lbSubredes.set(lbSubredes.get() + " " + str(2**datos[1]))
        lbHosts.set(lbHosts.get() + " " + str(2**datos[0] - 2))
        lbMask.set(lbMask.get() + " " + str(subredesL[0].netmask))
    elif opc == 2:
        ip = eIP.get()
        numsubs = int(eVal.get())
        clase = clasificarIP(ip)
        datos = usandoSubred(ip,numsubs)
        ip += netmask_class_a[clasificarIP(ip)]
        subredesL = list(ipaddress.ip_network(ip).subnets(new_prefix=datos[2]))
        lbClase.set(lbClase.get() + " " + str(clase))
        lbMaskP.set(lbMaskP.get() + " " + str(netmask_class_f[clase]))
        lbSubredes.set(lbSubredes.get() + " " + str(2**datos[1]))
        lbHosts.set(lbHosts.get() + " " + str(2**datos[0] - 2))
        lbMask.set(lbMask.get() + " " + str(subredesL[0].netmask))
    else:
        ip = eIP.get()
        prefijo = int(eVal.get())
        clase = clasificarIP(ip)
        ip += netmask_class_a[clasificarIP(ip)]
        subredesL = list(ipaddress.ip_network(ip).subnets(new_prefix=prefijo))
        datos = usandoSubred(ip,len(subredesL))
        lbClase.set(lbClase.get() + " " + str(clase))
        lbMaskP.set(lbMaskP.get() + " " + str(netmask_class_f[clase]))
        lbSubredes.set(lbSubredes.get() + " " + str(len(subredesL)))
        lbHosts.set(lbHosts.get() + " " + str(2**datos[0] - 2))
        lbMask.set(lbMask.get() + " " + str(subredesL[0].netmask))

def calcular():
    opc = variableRadio.get()
    if opc == 1:
        porHost()
    elif opc == 2:
        porSubred()
    else:
        porPrefijo()

def nuevo():
    eIP.set("")
    variableRadio.set("1")
    lbClase.set("")
    eVal.set("")
    lbClase.set("Clase IP:")
    lbMaskP.set("Mascara de Subred Predeterminada:")
    lbSubredes.set("Numero de Subredes:")
    lbHosts.set("Numero de Hosts por subred:")
    lbMask.set("Mascara de Subred:")
    subredes.delete('1.0', 'end')
    hosts.delete('1.0', 'end')

window = Tk()
window.title("Calculadora IP")

frame1 = LabelFrame(window)
frame1.grid(row=0, column=0, padx=10, pady=10)
Label(frame1, text="Ingrede la dirección IP").grid(row=0,column=0,padx=5,pady=5)
eIP = StringVar()
Entry(frame1, textvariable=eIP, validate='key', validatecommand=(window.register(isNumber),"%S")).grid(row=0,column=1,padx=5,pady=5)
Label(frame1, text="Valor:").grid(row=1,column=0,padx=5,pady=5)
eVal = StringVar()
Entry(frame1, textvariable=eVal, validate='key', validatecommand=(window.register(isNumber),"%S")).grid(row=1,column=1,padx=5,pady=5)
Button(frame1, text="CALCULAR", command=calcular).grid(row=2,column=0,columnspan=2,sticky=W+E,padx=5,pady=5)
Button(frame1, text="SOLO DATOS", command=datos).grid(row=3,column=0,columnspan=2,sticky=W+E,padx=5,pady=5)

frame2 = LabelFrame(window)
frame2.grid(row=0, column=1, padx=10, pady=10)
variableRadio = IntVar()
variableRadio.set("1")
Radiobutton(frame2,text="Host por Subred", variable=variableRadio, value=1).grid(row=0,column=0,padx=5,pady=5)
Radiobutton(frame2,text="Numero de Subredes", variable=variableRadio, value=2).grid(row=1,column=0,padx=5,pady=5)
Radiobutton(frame2,text="Usando un Prefijo", variable=variableRadio, value=3).grid(row=2,column=0,padx=5,pady=5)

frame3 = LabelFrame(window)
frame3.grid(row=0,column=2,padx=10,pady=10)
lbClase = StringVar()
lbClase.set("Clase IP:")
Label(frame3, textvariable=lbClase).grid(row=0,column=0,padx=5,pady=5)
lbMaskP = StringVar()
lbMaskP.set("Mascara de Subred Predeterminada:")
Label(frame3, textvariable=lbMaskP).grid(row=1,column=0,padx=5,pady=5)
lbSubredes = StringVar()
lbSubredes.set("Numero de Subredes:")
Label(frame3,textvariable=lbSubredes).grid(row=2,column=0,padx=5,pady=5)
lbHosts = StringVar()
lbHosts.set("Numero de Hosts por subred:")
Label(frame3,textvariable=lbHosts).grid(row=3,column=0,padx=5,pady=5)
lbMask = StringVar()
lbMask.set("Mascara de Subred:")
Label(frame3,textvariable=lbMask).grid(row=4,column=0,padx=5,pady=5)

frame4 = LabelFrame(window)
frame4.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
subredes = tkinter.scrolledtext.ScrolledText(frame4)
subredes.grid(row=0,column=0,padx=10,pady=10)
hosts = tkinter.scrolledtext.ScrolledText(frame4)
hosts.grid(row=0,column=1,padx=10,pady=10)
Button(frame4, text="NUEVO",command=nuevo).grid(row=1,column=0,padx=5,pady=5,columnspan=5,sticky=W+E)

window.mainloop()
