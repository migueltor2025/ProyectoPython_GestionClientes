import  tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


from componentes.interface import interface

root = ttk.Window(themename="flatly")
root.title("Sistema Modular de Clientes")
root.geometry("800x500")
root.resizable(False, False)


if '__main__' == __name__:
    interface(root=root)
    
    root.mainloop()  


