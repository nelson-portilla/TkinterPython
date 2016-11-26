from tkinter import *
import math
from PIL import Image, ImageTk

global matriz

#MATRIZ
#		nombre, 					abreviatura, pt, 		pf, 			pc
pet=["Polietilentereftalato",			"PET",	[130,200],	[81,100],	[8.6,10.0]]
pead=["Polietileno de alta densidad",	"PEAD",	[95,129],	[51,80],	[6.8,8.5]]
pvc=["Policloruro de vinilo",			"PVC",	[70,94],	[36,50],	[5.1,6.7]]
pebd=["Polietileno de baja densidad",	"PEBD",	[30,69],	[21,35],	[3.3,5.0]]
pp=["polipropileno",					"PP",	[10,29],	[6,20],		[1.5,3.2]]
ps=["poliestireno",						"PS",	[0,9],		[0,5],		[0,1.4]]

matriz=[pet,pead,pvc,pebd,pp,ps]

def guardar():
    print ("HOlA MUNDO")



# *************************************************** SISTEMA RECOMENDACION ******************
def crear_sistema_uno():
	def recomendar():
		textresultado.delete(0.1, END)
		valor_pt = float(textTraccion.get())
		valor_pf = float(textFlexion.get())
		valor_pc = float(textCompresion.get())
		
		materialpt="No Hay Material Para este valor"
		materialpf="No Hay Material Para este valor"
		materialpc="No Hay Material Para este valor"


		for i in range(0,6):
			matrizpt=matriz[i][2]
			matrizpf=matriz[i][3]
			matrizpc=matriz[i][4]
			
			if(matrizpt[0]<=valor_pt<=matrizpt[1]):
				materialpt=matriz[i][0]
			if(matrizpf[0]<=valor_pf<=matrizpf[1]):
				materialpf=matriz[i][0]
			if(matrizpc[0]<=valor_pc<=matrizpc[1]):
				materialpc=matriz[i][0]

		print (materialpt," ",materialpf," ",materialpc)

		textresultado.insert(0.1, "Los materiales recomendados para estas propiedades son:\n" + "PT: "+materialpt+"\n" + "PF: "+materialpf+"\n" + "PC: "+materialpc)

	### ****** GUI SISTEMA UNO *************	
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

	boton_sistema_uno = Button(frameBotones_s1,  text="Recomendar Material", command=recomendar, compound="left", state=NORMAL,
	                   bd=2, activebackground="#CCFFFF").grid(row=0, column=0)


	frameInformacion_s1.pack()
	frameDatos_s1.pack()
	frameCajon.pack()
	frameBotones_s1.pack()
	# gui_s1.mainloop()

# **************************************************** SISTEMA ENSAYOS******************



def crear_sistema_dos():

	def contar():		
		textresultado.delete(0.1, END)
		
		abreviatura=textNombreMaterial.get()
		listaPT=textResRT.get().split(",")
		listaPF=textResRF.get().split(",")
		listaPC=textResRC.get().split(",")

		print (listaPC)

		materialpt="No Hay Material Para este valor"
		materialpf="No Hay Material Para este valor"
		materialpc="No Hay Material Para este valor"

		countPT=0
		countPF=0
		countPC=0
		nombre="No Existe Abreviatura"

		for i in range(0,6):

			matrizpt=matriz[i][2]
			matrizpf=matriz[i][3]
			matrizpc=matriz[i][4]

			if(abreviatura.upper()==matriz[i][1]):
				nombre=matriz[i][0]

				for item in listaPT:
					if(matrizpt[0]<=int(item)<=matrizpt[1]):
						countPT=countPT+1

				for item in listaPF:
					if(matrizpf[0]<=int(item)<=matrizpf[1]):						
						countPF=countPF+1

				for item in listaPC:
					if(matrizpc[0]<=float(item)<=matrizpc[1]):
						countPC=countPC+1
			
		print (countPT," ",countPF," ",countPC)

		textresultado.insert(0.1, "El numero de ensayos para el "+nombre+" es:\n" + "PT: "+str(countPT)+"\n" + "PF: "+str(countPF)+"\n" + "PC: "+str(countPC))


	#####************ GUI SISTEMA DE ENSAYOS ***********
	gui_s2= Tk()
	gui_s2.title("SISTEMA DE ENSAYOS")
	frameInformacion_s2 = Frame(gui_s2)
	frameBotones_s2 = Frame(gui_s2)
	frameDatos_s2 = Frame(gui_s2)
	frameDatosNumero_s2 = Frame(gui_s2)
	frameDatosResultado_s2 = Frame(gui_s2)
	frameCajon2 = Frame(gui_s2)

	labelimagen_s2 = Label(frameInformacion_s2, text="").grid(row=0, column=0)
	labelinformacion_s2 = Label(frameInformacion_s2,
	                         text="Sistema de Ensayos",
	                         font = "Helvetica 11 bold italic",
	                         relief=SUNKEN).grid(row=1, column=0)
	labelespacio_s2 = Label(frameInformacion_s2, text="\n").grid(row=2, column=0)


	labelNombreMaterial = Label(frameDatos_s2, text="Abreviatura del Material\nPET,PEAD,PVC,PEBD,PP,PS").grid(row=0, column=0)
	textNombreMaterial = Entry(frameDatos_s2)
	textNombreMaterial.grid(row=0, column=1)
	labelinfo_s2 = Label(frameDatos_s2, text="Seleccione el tipo de ensayo", font = "Verdana 9 bold").grid(row=1, column=1)


	varRT = IntVar()
	checkRT = Checkbutton(frameDatos_s2, text="Traccion", variable=varRT, command=guardar).grid(row=2, column=0)
	varRF = IntVar()
	checkRF = Checkbutton(frameDatos_s2, text="Flexion", variable=varRF).grid(row=2, column=1)
	varRC = IntVar()
	checkRC = Checkbutton(frameDatos_s2, text="Compresion", variable=varRC).grid(row=2, column=2)

	
	labelinfo_s2 = Label(frameDatosNumero_s2, text="Digite el numero de ensayos de cada tipo", font = "Verdana 9 bold").grid(row=0, column=1)
	labelNumeroRT = Label(frameDatosNumero_s2, text="Traccion: ").grid(row=1, column=0)
	textNumeroRT = Entry(frameDatosNumero_s2)
	textNumeroRT.grid(row=1, column=1)

	labelNumeroRF = Label(frameDatosNumero_s2, text="Flexion: ").grid(row=2, column=0)
	textNumeroRF = Entry(frameDatosNumero_s2)
	textNumeroRF.grid(row=2, column=1)

	labelNumeroRC = Label(frameDatosNumero_s2, text="Compresion: ").grid(row=3, column=0)
	textNumeroRC = Entry(frameDatosNumero_s2)
	textNumeroRC.grid(row=3, column=1)


	labelinfoRes_s2 = Label(frameDatosResultado_s2, text="Digite el resultado de los ensayos separados por coma", font = "Verdana 9 bold").grid(row=0, column=1)
	labelinfoRes2_s2 = Label(frameDatosResultado_s2, text="EJ: 5,8,10.6,80", font = "Verdana 9 bold").grid(row=1, column=1)
	
	labelResRT = Label(frameDatosResultado_s2, text="Traccion: ").grid(row=2, column=0)
	textResRT = Entry(frameDatosResultado_s2)
	textResRT.grid(row=2, column=1)

	labelResRF = Label(frameDatosResultado_s2, text="Flexion: ").grid(row=3, column=0)
	textResRF = Entry(frameDatosResultado_s2)
	textResRF.grid(row=3, column=1)

	labelResRC = Label(frameDatosResultado_s2, text="Compresion: ").grid(row=4, column=0)
	textResRC = Entry(frameDatosResultado_s2)
	textResRC.grid(row=4, column=1)
	

	labelresultado = Label(frameCajon2, text="Resultado").grid(row=0, column=0)
	textresultado = Text(frameCajon2, height=12, width=60)
	textresultado.grid(row=1, column=0)


	boton_sistema_dos = Button(frameBotones_s2,  text="Cuantos Pasaron?", command=contar, compound="left", state=NORMAL,
	                   bd=2, activebackground="#CCFFFF").grid(row=0, column=0)


	frameInformacion_s2.pack()
	frameDatos_s2.pack()
	frameDatosNumero_s2.pack()
	frameDatosResultado_s2.pack()
	frameCajon2.pack()
	frameBotones_s2.pack()
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
boton_sistema_dos = Button(frameBotones, width=256, height=40, text="Sistema de Ensayos", command=crear_sistema_dos, compound="left", image=photo2, state=NORMAL,
                   bd=2, activebackground="#CCFFFF").grid(row=0, column=1)

frameInformacion.pack(side=TOP)
frameBotones.pack(side=BOTTOM)


gui.resizable(width=True, height=True)
gui.mainloop()
