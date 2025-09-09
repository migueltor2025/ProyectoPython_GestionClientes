import sqlite3
from tkinter import messagebox

# conexion = sqlite3.connect("clientes.db")  
# cursor = conexion.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS clientes (
#     
#     dni TEXT NOT NULL UNIQUE,
#     nombres TEXT NOT NULL,
#     apellidos TEXT NOT NULL,
#     telefono TEXT,
#     profecion TEXT NOT NULL
# );
               
# """)

# conexion.commit()
# conexion.close()
 
def conectar():
    try:
        conexion = sqlite3.connect("clientes.db")  
        cursor = conexion.cursor()
        cursor.execute("""Select * from clientes""")
        datos=cursor.fetchall()
        conexion.commit()
        conexion.close()
        return datos
    except:
        messagebox.showerror('Error conectar()','error al conectar sqlite3')


def registrar(datos):
    try:
        conexion = sqlite3.connect("clientes.db")  
        cursor = conexion.cursor()
        sql=("""INSERT INTO clientes(dni, nombres, apellidos, telefono, profecion)
             VALUES (?,?,?,?,?)""")
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()
    except sqlite3.IntegrityError as Error1:
        messagebox.showerror('Error registrar()', Error1)










# def peticion_grafica():
#     conexion = sqlite3.connect("clientes.db")  
#     cursor = conexion.cursor()
#     cursor.execute(f'''INSERT INTO clientes(dni, nombres, apellidos, telefono, profecion) 
#                     VALUES 
#                     ("34598723",	"KERVIN JHOJAN",	"APAZA ROSSI",	       "983920174",	  "Comercial"),
#                     ("98734123",	"FERNANDO",	         "CALCINA MASCO", 	  "928374615",	  "Camarero/a"),
#                     ("98723476",	"CRISTOPHER",	   "CALDERÓN GARZÓN" ,	  "902938475",	  "Camarero/a"),
#                     ("45678392",	"HANNES NUDT",	    "GONZÁLES RÍOS",	  "964738291",	  "Recepcionista"),
#                     ("37657482",	"MAYCOL RAYMUNDO",	"JUNCO BASURCO",	      "937261945",	  "Comercial"),
#                     ("28674821",	"JIMMY JESUS",	     "MAMANI HUANCA",	  "994857201",	  "Asesor/a fiscal"),
#                     ("20876545",	"DENILSON RIVALDO",	"MANGO PERALTA", 	  "948392615",	  "Administrativo/a"),
#                     ("26456401",	"MARÍA ROSA",	    "NUÑEZ  PRADO",	       "915293847",	  "Abogado/a"),
#                     ("26000276",	"PAOLA",	         "OBANDO ALEMAN",	   "920384756",	  "Camarero/a"),
#                     ("45093082",	"MARCO FABIÁN",	      "OBANDO LOAYZA", 	   "984756291",	  "Recepcionista"),
#                     ("27409489",	"SHEYLA",	           "OCHOA MANRIQUE",   "992837465",	  "Conductor/a"),
#                     ("36857484",	"NICOLE",	         "OSORIO PARIAPAZA",   "937465920",	  "Camarero/a"),
#                     ("36475800",	"ROLANDY",	         "PAREDES MONROY",	   "975920183",	  "Funcionario/a"),
#                     ("27465689",	"RENZO",	         "POLANCO  MORALES",   "993847561",	  "Conductor/a"),
#                     ("20345456",	"ALBERTO",	           "VALDIVIA LUNA",	   "961920384",	  "Recepcionista");''')
#     conexion.commit()
#     conexion.close()

# peticion_grafica()

