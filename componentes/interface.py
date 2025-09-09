import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from componentes.contenido import mostrar_contenido

def interface(root):

    
    
    # Cabecera fija
    cabecera = ttk.Frame(root, padding=10, bootstyle="primary")
    cabecera.pack(fill=X)
    ttk.Label(cabecera, text="🧾 Gestión de Clientes", font=("Arial", 18), bootstyle="inverse").pack(side=LEFT)

    # Contenedor principal
    contenedor = ttk.Frame(root)
    contenedor.pack(fill=BOTH, expand=True)

    # Menú lateral
    menu = ttk.Frame(contenedor, width=180, padding=10, bootstyle="secondary")
    menu.pack(side=LEFT, fill=Y)

    ttk.Label(menu, text="Menú", font=("Arial", 12), bootstyle="inverse").pack(pady=5)
    ttk.Button(menu, text="Inicio", bootstyle="info-outline", command=lambda: mostrar_contenido("inicio", contenido)).pack(fill=X, pady=2)
    ttk.Button(menu, text="Clientes", bootstyle="info-outline", command=lambda: mostrar_contenido("clientes", contenido)).pack(fill=X, pady=2)
    ttk.Button(menu, text="Reportes", bootstyle="info-outline", command=lambda: mostrar_contenido("reportes", contenido)).pack(fill=X, pady=2)

    # Área de contenido dinámico
    contenido = ttk.Frame(contenedor, padding=20)
    contenido.pack(side=LEFT, fill=BOTH, expand=True)

    # Mostrar vista inicial
    mostrar_contenido("inicio", contenido)

    return 