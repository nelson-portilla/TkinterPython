from tkinter import *
import math
from PIL import Image, ImageTk

global listadenumeros, cont, prom, varianzafinal, desviacionfinal
cont = 0
listadenumeros = []
prom=0.0
varianzafinal=0.0
desviacionfinal=0.0


def guardar():
    print ("HOlA MUNDO")


# **************************************************** GUI SISTEMA RECOMENDACIO N******************
def crear_sistema_uno():
	gui_s1= Tk()
	gui_s1.title("SISTEMA DE RECOMENDACION")
	frameInformacion_s1 = Frame(gui_s1)
	frameBotones_s1 = Frame(gui_s1)
	frameDatos_s1 = Frame(gui_s1)
	frameCajon = Frame(gui_s1)

	labelimagen_s1 = Label(frameInformacion_s1, text="").grid(row=0, column=0)
	labelinformacion_s1 = Label(frameInformacion_s1,
	                         text="Sistema de Recomendacion",
	                         font = "Helvetica 11 bold italic",
	                         relief=SUNKEN).grid(row=1, column=0)

	labelespacio_s1 = Label(frameInformacion_s1, text="\n").grid(row=2, column=0)

	labelinfo_s1 = Label(frameInformacion_s1, text="Digite los respectivos valores en cada caracteristica", font = "Verdana 9 bold").grid(row=3, column=0)

	labelTraccion = Label(frameDatos_s1, text="Traccion: ").grid(row=0, column=0)
	textTraccion = Entry(frameDatos_s1)
	textTraccion.grid(row=0, column=1)

	labelFlexion = Label(frameDatos_s1, text="Flexion: ").grid(row=1, column=0)
	textFlexion = Entry(frameDatos_s1)
	textFlexion.grid(row=1, column=1)

	labelCompresion = Label(frameDatos_s1, text="Compresion: ").grid(row=2, column=0)
	textCompresion = Entry(frameDatos_s1)
	textCompresion.grid(row=2, column=1)

	labelresultado = Label(frameCajon, text="Resultado").grid(row=0, column=0)
	textresultado = Text(frameCajon, height=12, width=60)
	textresultado.grid(row=1, column=0)

	boton_sistema_uno = Button(frameBotones_s1,  text="Recomendar Material", command=guardar, compound="left", state=NORMAL,
	                   bd=2, activebackground="#CCFFFF").grid(row=0, column=0)


	frameInformacion_s1.pack()
	frameDatos_s1.pack()
	frameCajon.pack()
	frameBotones_s1.pack()
	# gui_s1.mainloop()


# **************************************************** GUI PRINCIPAL ******************

gui = Tk()
# gui.geometry("750x330+0+0")
gui.title("CONTROL DE CALIDAD - PLASTICOS")

frameInformacion = Frame(gui)
frameBotones = Frame(gui)

logo_sistema = PhotoImage(file='ImagenSistema3.gif')
labelimagen = Label(frameInformacion, text="", image=logo_sistema).grid(row=0, column=0)
labelinformacion = Label(frameInformacion,
                         text="CONTROL DE CALIDAD - PLASTICOS\n karen Echeverry \nCamila Caicedo\nLuna Rodrigo",
                         font = "Helvetica 11 bold italic",
                         relief=SUNKEN).grid(row=1, column=0)

labelespacio = Label(frameInformacion, text="\n").grid(row=2, column=0)

labelinfo = Label(frameInformacion, text="Seleccione el sistema que desea utilizar", font = "Verdana 9 bold").grid(row=3, column=0)

####Marco donde estan los botones
icon_sistema_uno = Image.open('ImagenSistema1.gif')
icon_sistema_dos = Image.open('ImagenSistema4.gif')
logo=icon_sistema_uno.resize((60, 40), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(logo)
logo2=icon_sistema_dos.resize((60, 40), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(logo2)

boton_sistema_uno = Button(frameBotones, width=256, height=40, text="Sistema de Recomendacion", command=crear_sistema_uno, compound="left", image=photo, state=NORMAL,
                   bd=2, activebackground="#CCFFFF").grid(row=0, column=0)
boton_sistema_dos = Button(frameBotones, width=256, height=40, text="Sistema de Ensayos", command=guardar, compound="left", image=photo2, state=NORMAL,
                   bd=2, activebackground="#CCFFFF").grid(row=0, column=1)

frameInformacion.pack(side=TOP)
frameBotones.pack(side=BOTTOM)


gui.resizable(width=True, height=True)
gui.mainloop()
