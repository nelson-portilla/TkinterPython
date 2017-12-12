import os,sys
import time as control_time
#PARA WINDOWS DESCARGAR DRIVER http://www.stickpeople.com/projects/python/win-psycopg/
#PARA LINUX COMANDO: pip install psycopg2
import psycopg2
import string
import random
#PARA Python 2.7 
# import Tkinter as Tk
from Tkinter import *
#PARA python 3
#from tkinter import tk


#CLASE PRINCIPAL
class Aplicacion(object):
	#VARIABLE PARA LA CONEXION
	con = None
	#VARIABLE PARA EL CURSOR QUE EJECUTA LAS CONSULTAS
	cur = None



	#CONSTRUCTOR DONDE SE INICIALIZA LA CONEXION A LA BD, EN CASO DE FALLO, SE INDICA EL ERROR
	def __init__(self, textArea):
		#SIEMPRE SE BORRA EL CONTENIDO QUE ESTA ALMACENADO EN EL TEXTAREA
		textArea.delete(0.1, END)		
		try:
			#SE ESTABLECEN LOS PARAMETROS PARA LA BD
			self.con = psycopg2.connect(database="autos uv", user="registro", password="rpcc1") 
			self.cur = self.con.cursor()
			self.cur.execute('SELECT version()')          
			ver = self.cur.fetchone()
			print("Conexion a base de datos exitosa "+str(ver))
			textArea.insert(END, "Conexion a base de datos exitosa "+str(ver))
		except psycopg2.DatabaseError as e:
			print("Fallo en la conexion a base de datos, revise parametros de configuracion")
			textArea.insert(END, "Fallo en la conexion a base de datos, revise parametros de configuracion en config/config")
			print("Error: "+str(e))
			textArea.insert(END, "Error: "+str(e))
			sys.exit(1)

	##METODO Punto Uno Opcion de consulta UNO
	def opcion_de_consulta_uno(self, textArea):
		#SIEMPRE SE BORRA EL CONTENIDO QUE ESTA ALMACENADO EN EL TEXTAREA
		textArea.delete(0.1, END)
		try:
			sql="select placa from vehiculo as v,reserva as r,listareserva as l where "+\
								"r.cliente in "+\
									"(select nitcli from cliente where ciudad='Bogota') "+\
								"and v.placa=l.placavehic "+\
								"and r.numeror=l.reserva"
			self.cur.execute(sql)
			rows = self.cur.fetchall()
			textArea.insert(END, "*CONSULTA NUMERO UNO*\n")
			textArea.insert(END, "Obtener la placa del vehiculo de aquellos vehiculos vendidos a clientes de Bogota\n")
			textArea.insert(END, "*CONSULTA:*\n")
			textArea.insert(END, sql)
			textArea.insert(END, "\n*RESULTADO:*\n")
			textArea.insert(END, rows)
			
		except psycopg2.DatabaseError as e:
			print("Fallo en la consulta consultar_ciudad")
			print("Error: "+str(e))
			sys.exit(1)			
		except psycopg2.InterfaceError as ie:
			print("Fallo en la consulta ciudad")
			print("Error: "+str(ie))
			sys.exit(1)

	##METODO Punto Uno Opcion de consulta DOS
	def opcion_de_consulta_dos(self, textArea):
		#SIEMPRE SE BORRA EL CONTENIDO QUE ESTA ALMACENADO EN EL TEXTAREA
		textArea.delete(0.1, END)
		try:
			sql="select distinct codigo,nombre,direccion,ciudad from agencia as a,reserva as r,listareserva as l where "+\
				"l.placavehic not in "+\
				"(select placavehic from agencia,reserva,listareserva where agencia.ciudad='Cali' "+\
				"and agencia.codigo=reserva.agencia and reserva.numeror=listareserva.reserva) " +\
				"and a.codigo=r.agencia " +\
				"and r.numeror=l.reserva"
			self.cur.execute(sql)
			rows = self.cur.fetchall()
			textArea.insert(END, "*CONSULTA NUMERO DOS*\n")
			textArea.insert(END, "Info de las agencias que no venden los vehiculos que venden las agencias de Cali\n")
			textArea.insert(END, "*CONSULTA:*\n")
			textArea.insert(END, sql)
			textArea.insert(END, "\n*RESULTADO:*\n")
			textArea.insert(END, rows)
			
		except psycopg2.DatabaseError as e:
			print("Fallo en la consulta consultar_ciudad")
			print("Error: "+str(e))
			sys.exit(1)			
		except psycopg2.InterfaceError as ie:
			print("Fallo en la consulta ciudad")
			print("Error: "+str(ie))
			sys.exit(1)


	#METODO PARA INSERTAR 10 VEHICULOS ALEATORIAMENTE
	def insertar_vehiculos(self, textArea):
			#SIEMPRE SE BORRA EL CONTENIDO QUE ESTA ALMACENADO EN EL TEXTAREA
			textArea.delete(0.1, END)
			#MENSAJE QUE SE CONTENDRA LAS PLACAS INSERTADAS PARA MOSTRARLAS
			mensaje=""

			#LISTA DE MARCAS
			marcas=["Mazda", "Chevrolet", "Audi", "Ford", "Nissan"]
			#LISTA DE MODELOS
			modelos=["v8", "sentra", "a7", "m6", "sparkgt", "fiesta", "cx9", "explorer"]
			#LISTA DE COLORES
			colores=["Negro","Blanco","Rojo","Gris","Azul"]
			#LISTA DE GARAJES, SE SUPONE QUE ESTOS GARAJES YA ESTA INSERTADOS
			garajes=["g001","g002"]
			#LETRAS DEL ABECEDARIO PARA LAS PLACAS
			letras = string.ascii_lowercase
			#CICLO QUE CREA VEHICULOS ALEATORIOS CON ITEMS ALEATORIOS DE LAS LISTAS ANTERIORES
			for i in range (0, 10):
				#GENERA UNA SERIE DE LETRAS ALEATORIAS DE TRES DIGITOS
				serie=''.join(random.choice(letras) for i in range(3))
				#GENERA NUMERO DE TRES DIGITOS ALEATORIO
				numero=random.randint(100,999)
				
				placa=serie+"-"+str(numero)
				mensaje+=placa+"\n"
				marca=marcas[random.randint(0,4)]
				modelo=modelos[random.randint(0,7)]
				color=colores[random.randint(0,4)]
				garaje=garajes[random.randint(0,1)]
				precio=random.randint(1000,10000)
				auto=[placa,marca,modelo,color,garaje,precio]
				try:
					#SE EJECUTA EL CODIGO SQL POR MEDIO DEL JDBC, se definen las columnas y los valores a insertar
					self.cur.execute('INSERT INTO vehiculo (placa, marca, modelo, color, garaje, precioalquiler) VALUES (%s,%s,%s,%s,%s,%s)', auto)
					#SE REALIZA UN COMMIT PARA INDICAR CAMBIOS EN LA BD
					self.con.commit()		
				except psycopg2.DatabaseError as e:
					print("Fallo en la consulta")
					print("Error: "+str(e))
					sys.exit(1)			
				except psycopg2.InterfaceError as ie:
					print("Fallo en la consulta, se ha cerrado la conexion")
					print("Error: "+str(ie))
					sys.exit(1)

			#SE MUESTRA EL MENSAJE					
			textArea.insert(END, "*SE INSERTARON LAS SIGUIENTES PLACAS*\n")
			textArea.insert(END, mensaje)

	##METODO Punto 3 Opcion de modificacion SE ASUME QUE ESTAN INSERTADOS LOS SIG CLIENTES NIT
	def modificar_cliente(self, textArea):
		#SIEMPRE SE BORRA EL CONTENIDO QUE ESTA ALMACENADO EN EL TEXTAREA
		textArea.delete(0.1, END)
		mensaje=""

		try:
			lista_cedulas=["1111","1122","1133","1144","1155"]
			rowcount=0
			#EN ESTE CICLO SE ACTUALIZAN LA CIUDAD CALI A LAS CINCO CEDULAS EN LA LISTA
			for cedula in lista_cedulas:
					#EL UPDATE TIENE DOS PUNTEROS, EL PRIMERO ES PARA LA CIUDAD y EL OTRO PARA EL nit
					#AL FINAL SE RECIBE UNA DUPLA CON LOS VALORES (CALI, cedula)				
					self.cur.execute("UPDATE cliente SET ciudad=(%s) WHERE nitcli = (%s)", ("Cali",cedula))
					#SE VA ACUMULANDO LAS DUPLAS AFECTADAS
					rowcount += self.cur.rowcount;
			#SE ACTUALIZA LA BD
			self.con.commit()		
			if rowcount>0:
				textArea.insert(END, "\n*SE MODIFICARON LA CIUDAD EN +"+str(rowcount)+"* tuplas de cliente\nLas cedulas modificadas son:\n")
				textArea.insert(END, lista_cedulas)
				print ("Se modificaron la ciudad en "+str(rowcount)+" tuplas")
			else:
				textArea.insert(END, "No se modificaron registros")
				print ("No se modificaron registros")

			#EN ESTA INSTRUCCION SE ACTUALIZA UNA DIRECCION
			self.cur.execute("UPDATE cliente SET direccion=(%s) WHERE nitcli = (%s)", ("Calle 80 N 100 01",1166))
			#SE OBTIENE LAS DUPLAS AFECTADAS
			rowcount = self.cur.rowcount;
			self.con.commit()		
			if rowcount>0:
				print ("Se modificaron la direccion en "+str(rowcount)+" tuplas")
			else:
				print ("No se modificaron registros")


		except psycopg2.DatabaseError as e:
			print("Fallo en la consulta consultar_ciudad")
			print("Error: "+str(e))
			sys.exit(1)			
		except psycopg2.InterfaceError as ie:
			print("Fallo en la consulta ciudad")
			print("Error: "+str(ie))
			sys.exit(1)

	##METODO Punto 4 Opcion de borrado SE ASUME QUE ESTAN REGISTRADOS LAS AGENCIAS 1 2 3
	def borrar_agencia(self,textArea):
		#SIEMPRE SE BORRA EL CONTENIDO QUE ESTA ALMACENADO EN EL TEXTAREA
		textArea.delete(0.1, END)
		mensaje=""
		try:
			#ESTE ES UN CONTADOR PARA DUPLAS AFECTADAS
			rowcount=0
			#LOS CODIGOS DE LAS AGENCIAS SON CONSECUTIVOS 1 2 3 
			for codigo in range(1,4):
					#DENTRO DEL CICLO BORRAMOS CADA REGISTRO CON CODIGO 1 2 3				
					self.cur.execute("DELETE FROM agencia WHERE codigo="+str(codigo))
					#SE VA ACUMULANDO LAS DUPLAS AFECTADAS
					rowcount += self.cur.rowcount;
					mensaje +=str(codigo)+"\n"
			#SE REALIZA EN CAMBIO EN LA BD
			self.con.commit()		
			if rowcount>0:
				textArea.insert(END, "\n*SE ELIMINARON +"+str(rowcount)+"* tuplas\nLas agencias borradas son:\n")
				textArea.insert(END, mensaje)
				print ("Se eliminaron "+str(rowcount)+" agencias")
			else:
				print ("No se eliminaron registros")
		except psycopg2.DatabaseError as e:
			print("Fallo en la consulta consultar_ciudad")
			print("Error: "+str(e))
			sys.exit(1)			
		except psycopg2.InterfaceError as ie:
			print("Fallo en la consulta ciudad")
			print("Error: "+str(ie))
			sys.exit(1)

	# OPCION DE LISTADO de tablas trabajadas
	def listar_tablas(self, textArea):
		#SIEMPRE SE BORRA EL CONTENIDO QUE ESTA ALMACENADO EN EL TEXTAREA
		textArea.delete(0.1, END)
		try:
			#LISTAMOS TODOS LOS ATRIBUTOS DE LA TABLA CLIENTE
			self.cur.execute('select * from cliente')
			rows = self.cur.fetchall()
			print (rows)
			textArea.insert(END, "*CLIENTES*\n")
			textArea.insert(END, rows)

			self.cur.execute('select * from vehiculo')
			rows = self.cur.fetchall()
			textArea.insert(END, "\n\n*VEHICULOS*\n")
			textArea.insert(END, rows)

			self.cur.execute('select * from agencia')
			rows = self.cur.fetchall()
			print (rows)
			textArea.insert(END, "\n\n*AGENCIAS*\n")
			textArea.insert(END, rows)
		except psycopg2.DatabaseError as e:
			print("Fallo en la consulta consultar_ciudad")
			print("Error: "+str(e))
			sys.exit(1)			
		except psycopg2.InterfaceError as ie:
			print("Fallo en la consulta ciudad")
			print("Error: "+str(ie))
			sys.exit(1)

	# CREAR ARCHIVO PLANO CON mas de 5000 REGISTROS
	def crear_plano_csv(self):
		#CREA EL ARCHIVO PLANO
		file=open("data_clientes.csv", "w")
		for i in range(1,5002):
			#SE CREAN CEDULAS ALEATORIAS
			file.write(str(random.randint(100000000,999999999))+",")
			#SE CREA NOMBRE 
			file.write("cliente_"+str(i)+",")
			file.write("direccion_"+str(i)+",")
			file.write("ciudad_"+str(i)+",")
			file.write(str(random.randint(10000,99999)))
			file.write("\n")
		file.close()
	
	# INSERTAR DATOS DESDE ARCHIVO PLANO
	def insertar_desde_plano_csv(self, textArea):
		#SIEMPRE SE BORRA EL CONTENIDO QUE ESTA ALMACENADO EN EL TEXTAREA
		textArea.delete(0.1, END)
		mensaje=0
		self.crear_plano_csv()
		SQL_STATEMENT = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
		my_file = open("data_clientes.csv", 'r')
		for linea in my_file:
			try:
				textArea.insert(END, "\n\n* "+str(mensaje)+" cliente insertado*\n")
				self.cur.execute('INSERT INTO cliente (nitcli, nombre, direccion, ciudad, telefono) VALUES (%s,%s,%s,%s,%s)', linea.split(","))
				self.con.commit()
				mensaje+=1
			except psycopg2.IntegrityError as ie:
				textArea.insert(END, "\n\n* "+str(mensaje)+" DATOS CARGADOS EXITOSAMENTE*\n")
				break
		textArea.insert(END, "\n\n* "+str(mensaje)+" DATOS CARGADOS EXITOSAMENTE*\n")


	#METODO PARA CERRAR CONEXION
	def cerrar(self):
		print ("SESION CERRADA")
		self.con.close()


if __name__ == '__main__':


	root = Tk()
	textArea = Text(root, height=40, width=100)
	textArea.pack(side=LEFT, fill=Y)
	scroll = Scrollbar(root)
	scroll.pack(side=RIGHT, fill=Y)
	scroll.config(command=textArea.yview)
	textArea.config(yscrollcommand=scroll.set)
	
	app=Aplicacion(textArea)

	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Opcion De consulta Uno", command=lambda:app.opcion_de_consulta_uno(textArea))
	filemenu.add_command(label="Opcion De consulta DOS", command=lambda:app.opcion_de_consulta_dos(textArea))
	filemenu.add_command(label="sql de Insercion", command=lambda:app.insertar_vehiculos(textArea))
	filemenu.add_command(label="sql de modificacion", command=lambda:app.modificar_cliente(textArea))
	filemenu.add_command(label="sql de borrado", command=lambda:app.borrar_agencia(textArea))
	filemenu.add_command(label="Listar Tablas", command=lambda:app.listar_tablas(textArea))
	filemenu.add_command(label="Cargar desde ARCHIVO plano", command=lambda:app.insertar_desde_plano_csv(textArea))
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=root.quit)
	menubar.add_cascade(label="Opciones", menu=filemenu)
	editmenu = Menu(menubar, tearoff=0)
	root.config(menu=menubar)
	
	root.title("Autos UV")
	root.mainloop()

		
	# app.insertar_vehiculos()
	# app.modificar_cliente()
	# app.borrar_agencia()
	# app.listar_tablas()
	# app.crear_plano_csv()
	# app.insertar_desde_plano_csv()
	app.cerrar()

