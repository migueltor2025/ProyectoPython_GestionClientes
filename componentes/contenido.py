import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from tkinter import ttk as tkttk
from componentes.conexion_sql import conectar, registrar
import re
def mostrar_contenido(tipo, contenido):
    for widget in contenido.winfo_children():
        widget.destroy()

    if tipo == "clientes":
        ttk.Label(contenido, text="Formulario de Cliente", font=("Arial", 14), bootstyle="primary").pack(pady=10)


        ttk.Label(contenido, text="Dni:").pack(anchor=W, pady=5)
        entry_dni = ttk.Entry(contenido, width=50)
        entry_dni.pack()

        ttk.Label(contenido, text="Nombres:").pack(anchor=W, pady=5)
        entry_nombres = ttk.Entry(contenido, width=50)
        entry_nombres.pack()

        ttk.Label(contenido, text="Apellidos:").pack(anchor=W, pady=5)
        entry_apellidos = ttk.Entry(contenido, width=50)
        entry_apellidos.pack()

        ttk.Label(contenido, text="Teléfono:").pack(anchor=W, pady=5)
        entry_telefono = ttk.Entry(contenido, width=50)
        entry_telefono.pack()

        ttk.Label(contenido, text="Profecion:").pack(anchor=W, pady=5)
        entry_profecion = ttk.Entry(contenido, width=50)
        entry_profecion.pack()

        

        def registrar_cliente():
            try:
                # valida 8 digitos del dni
                def validar_dni(dni: str) -> bool:
                    return bool(re.fullmatch(r"\d{8}", dni))
                
                dni = entry_dni.get() if validar_dni(entry_dni.get())==True else None
                      
                # valida 9 digitos de telefono
                def validar_telefono(telefono: str) -> bool:
                    return bool(re.fullmatch(r"\d{9}", telefono))
                
                telefono = entry_telefono.get() if validar_telefono(entry_telefono.get())==True else None
                    
                # valida que los campos sean string    
                def validar_text(texto: str) -> bool:
                    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", texto))
                nombres = entry_nombres.get().upper() if validar_text(entry_nombres.get())==True else None
                apellidos = entry_apellidos.get().upper() if validar_text(entry_apellidos.get())==True else None
                profecion = entry_profecion.get().upper() if validar_text(entry_profecion.get())==True else None

                datos = dni, nombres, apellidos, telefono, profecion
                
                    
            except:
                print('El dni o el telefono tiene caracteres no numericos, no se registro')
                

            try:
                entry_dni.delete(0, END)
                entry_nombres.delete(0, END)
                entry_apellidos.delete(0, END)
                entry_telefono.delete(0, END)
                entry_profecion.delete(0, END)
                registrar(datos)
                messagebox.showinfo("Registro exitoso", f"Cliente registrado:\nNombre: {nombres} {apellidos}\nTeléfono: {telefono}")
            except:
                messagebox.showerror("Error al registrarr", "Comunicate con un administrador")

        ttk.Button(contenido, text="Registrar", bootstyle="success", command=registrar_cliente).pack(pady=20)

    elif tipo == "reportes":
        # Datos simulados
        clientes = conectar()

        # Contenedor principal
        contenedor = ttk.Frame(contenido)
        contenedor.pack(fill=BOTH, expand=True)

        # buscador de contenido*********************************************************

        buscador_frame = ttk.Frame(contenido)
        buscador_frame.pack(fill=X, pady=5)

        ttk.Label(buscador_frame, text="🔍 Buscar cliente:", font=("Arial", 10)).pack(side=LEFT, padx=5)
        entry_busqueda = ttk.Entry(buscador_frame, width=30)
        entry_busqueda.pack(side=LEFT, padx=5)

        def buscar():
            
            consulta = entry_busqueda.get().lower()
            tabla.delete(*tabla.get_children())  
            
            for cliente in clientes:
                datos = [str(datos).lower() for datos in cliente]

                if any(consulta in campo for campo in datos):
                    tabla.insert("", END, values=cliente)

        ttk.Button(buscador_frame, text="Buscar", bootstyle="info", command=buscar).pack(side=LEFT, padx=5)
        # *********************************************************************************************

        # Panel de contenido
        contenido = ttk.Frame(contenedor, padding=20)
        contenido.pack(side=LEFT, fill=BOTH, expand=True)

        # Métricas rápidas
        metricas = ttk.Frame(contenido)
        metricas.pack(fill=X, pady=10)

        ttk.Label(metricas, text=f"Total clientes: {len(clientes)}", font=("Arial", 12), bootstyle="success").pack(side=LEFT, padx=10)
        #ttk.Label(metricas, text="Correos únicos: 4", font=("Arial", 12), bootstyle="info").pack(side=LEFT, padx=10)
        ttk.Label(metricas, text="Última actualización: Hoy", font=("Arial", 12), bootstyle="warning").pack(side=LEFT, padx=10)

        # Tabla de clientes
        tabla = tkttk.Treeview(contenido, columns=("DNI","Nombres","Apellidos", "Teléfono", "Profecion",), show="headings", height=10)
        tabla.pack(fill=BOTH, expand=True, pady=10)

        
        tabla.heading("DNI", text="DNI")
        tabla.heading("Nombres", text="Nombres")
        tabla.heading("Apellidos", text="Apellidos")
        tabla.heading("Teléfono", text="Teléfono")
        tabla.heading("Profecion", text="Profesión")

        
        tabla.column("DNI", width=7)
        tabla.column("Nombres", width=30)
        tabla.column("Apellidos", width=30)
        tabla.column("Teléfono", width=9)
        tabla.column("Profecion", width=30)



        for cliente in clientes:
            tabla.insert("", END, values=cliente)


    elif tipo == "inicio":
        ttk.Label(contenido, text="Bienvenido al sistema", font=("Arial", 14), bootstyle="secondary").pack(pady=10)
        ttk.Label(contenido, text="Selecciona una opción del menú lateral.").pack(pady=5)