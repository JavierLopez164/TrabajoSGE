import tkinter as tk
from tkinter import ttk
from clases.ventana import Ventana

ventana = Ventana(800, 600, "Trabajo SGE", 100, 100)

ventana.newLabel("Gestión de almacén", ventana.cabecera, "center", 20)

ventana.newLabel("Menú: ", ventana.izquierda, "center", 15)
ventana.botonGrafica(ventana.izquierda)
ventana.botonEmail(ventana.izquierda)
ventana.botonProducto(ventana.izquierda)

ventana.newLabel("© Raúl García\n © Javier López", ventana.pie, "w", 10)



ventana.mainloop()