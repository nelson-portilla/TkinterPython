from tkinter import *
import math

global listadenumeros, cont, prom, varianzafinal, desviacionfinal
cont = 0
listadenumeros = []
prom=0.0
varianzafinal=0.0
desviacionfinal=0.0


# def cargar():
#     global listadenumeros
#     cantidadnumeros=int(textcantidad.get())
#     listadenumeros=[]
#     textcantidad.delete(0,END)
#     textcantidad.insert(END,"Cargado")
#     botonCargar.config(state=DISABLED)
#     botonGuardar.config(state=NORMAL)


def guardar():
    global listadenumeros, cont
    valor = int(textnumero.get())
    listadenumeros.append(valor)
    textnumero.delete(0, END)
    cont = cont + 1
    mensaje = str(cont) + " numeros guardados"

    textocontador.set(mensaje)

    print(listadenumeros)


def moda():
    textresultado.delete(0.1, END)
    print(listadenumeros)
    #ordenado = sorted(listadenumeros)

    repeticiones = 0
    for i in listadenumeros:
        apariciones = listadenumeros.count(i)
        if apariciones > repeticiones:
            repeticiones = apariciones

    modas = []
    for i in listadenumeros:
        apariciones = listadenumeros.count(i)
        if apariciones == repeticiones and i not in modas:
            modas.append(i)

    print("moda: ", modas)
    textresultado.insert(0.1, "La Moda es: " + str(modas))
    #print(ordenado)


def varianza():

    textresultado.delete(0.1, END)

    prom = sum(listadenumeros) / len(listadenumeros)
    suma = 0
    for i in range(0, len(listadenumeros)):
        suma += ((listadenumeros[i] - prom) ** 2)
    varianzafinal = suma / len(listadenumeros)
    print(varianzafinal)
    textresultado.insert(0.1, "La Varianza es: " + str(varianzafinal))


def desviacion():
    textresultado.delete(0.1, END)

    prom = sum(listadenumeros) / len(listadenumeros)
    suma = 0
    for i in range(0, len(listadenumeros)):
        suma += ((listadenumeros[i] - prom) ** 2)
    varianzafinal = suma / len(listadenumeros)
    desviacionfinal = math.sqrt(varianzafinal)
    textresultado.insert(0.1, "La Varianza es: " + str(desviacionfinal))


def promedio():

    textresultado.delete(0.1, END)
    prom = sum(listadenumeros) / len(listadenumeros)

    textresultado.insert(0.1, "El promedio es: " + str(prom))


def mayor():
    textresultado.delete(0.1, END)
    mayornumero=max(listadenumeros)
    textresultado.insert(0.1, "El mayor es: "+str(mayornumero))
	


def menor():
    textresultado.delete(0.1, END)
    menornumero=min(listadenumeros)
    textresultado.insert(0.1, "El menor es: "+str(menornumero))


def imprimir():
    textresultado.delete(0.1, END)
    textresultado.insert(0.1, listadenumeros)


# **************************************************** GUI ******************

gui = Tk()
# gui.geometry("750x330+0+0")
gui.title("MINIPROYECTO ESTADISTICO")

frameInformacion = Frame(gui)
frameDatos = Frame(gui)
frameBotones = Frame(gui)
frameCajon = Frame(gui)

photo = PhotoImage(file='graficas.gif')
labelimagen = Label(frameInformacion, text="", image=photo).grid(row=0, column=0)
labelinformacion = Label(frameInformacion,
                         text="MINIPROYECTO ESTADISTICO\n Angelica Rivas \nDanna Gonzalez\nNatalia Osorio",
                         relief=SUNKEN).grid(row=1, column=0)

labelespacio = Label(frameInformacion, text="\n").grid(row=2, column=0)

labelnumero = Label(frameInformacion, text="Digite Numero").grid(row=3, column=0)
textnumero = Entry(frameInformacion)
textnumero.grid(row=4, column=0)

textocontador = StringVar()
textocontador.set("0 numeros guardados")
labelcontador = Label(frameInformacion, text="0 numeros guardados", textvariable=textocontador,
                      font=("Helvetica", 10)).grid(row=5, column=0)

labelresultado = Label(frameCajon, text="Resultado").grid(row=0, column=0)
textresultado = Text(frameCajon, height=12, width=60)
textresultado.grid(row=1, column=0)

####Marco donde estaán los botones
bticon = PhotoImage(file='arrow-icon.gif')
iconguardar = PhotoImage(file='add-icon.gif')

botonGuardar = Button(frameInformacion, text="Guardar", command=guardar, compound="left", image=iconguardar,
                      state=NORMAL, bg="#CCFFFF").grid(row=6, column=0)

labelresultado = Label(frameBotones, text="-OPERACIONES-", font=("Helvetica", 11)).grid(row=0, column=0)
botonModa = Button(frameBotones, width=130, text="Moda", command=moda, compound="left", image=bticon, state=NORMAL,
                   bd=2, activebackground="#CCFFFF").grid(row=1, column=0)
botonVarianza = Button(frameBotones, width=130, text="Varianza", command=varianza, compound="left", image=bticon,
                       state=NORMAL, bd=2, activebackground="#CCFFFF").grid(row=2, column=0)
botonDesviacion = Button(frameBotones, width=130, text="Desviacion Estandar", command=desviacion, compound="left",
                         image=bticon, state=NORMAL, bd=2, activebackground="#CCFFFF").grid(row=3, column=0)
botonPromedio = Button(frameBotones, width=130, text="Promedio", command=promedio, compound="left", image=bticon,
                       state=NORMAL, bd=2, activebackground="#CCFFFF").grid(row=4, column=0)
botonMayor = Button(frameBotones, width=130, text="Mayor", command=mayor, compound="left", image=bticon, state=NORMAL,
                    bd=2, activebackground="#CCFFFF").grid(row=5, column=0)
botonMenor = Button(frameBotones, width=130, text="Menor", command=menor, compound="left", image=bticon, state=NORMAL,
                    bd=2, activebackground="#CCFFFF").grid(row=6, column=0)
botonVerLista = Button(frameBotones, width=130, text="Imprimir Lista", command=imprimir, compound="left", image=bticon,
                       state=NORMAL, bd=2, activebackground="#CCFFFF").grid(row=7, column=0)
botonSalir = Button(frameBotones, width=130, text="Salir", command=gui.destroy, compound="left", image=bticon,
                    state=NORMAL, bd=2, activebackground="#CCFFFF").grid(row=8, column=0)

frameInformacion.pack(side=LEFT, fill=Y)
frameBotones.pack(side=LEFT, fill=Y, padx=20)
frameCajon.pack(side=LEFT, fill=BOTH)

gui.resizable(width=True, height=True)
gui.mainloop()
############################################################
