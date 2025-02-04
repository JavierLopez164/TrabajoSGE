import tkinter as tk
from tkinter import ttk
from herramientas import coloresAplicacion

class Ventana(tk.Tk):
    def __init__(self, ancho, alto, titulo, posx, posy):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
        self.titulo = titulo
        self.posx = posx
        self.posy = posy

        self.title(self.titulo)
        cA = coloresAplicacion()
        self.Color_principal = cA.get_Color_Principal()
        self.Color_pie = cA.get_Color_Pie()
        self.Color_izquierda = cA.get_Color_Izquierda()
        self.Color_cabecera = cA.get_Color_Cabecera()
        self.geometry(f"{self.ancho}x{self.alto}+{self.posx}+{self.posy}")
        self.resizable(True, True)
        self.cajas()
    
    def cajas(self):
        self.cabecera = tk.Frame(
            self,
            bg = self.Color_cabecera,
            height = 60,
        )
        self.cabecera.pack(side = tk.TOP, fill = "both")
        self.cabecera.propagate(False)

        self.pie = tk.Frame(
            self,
            bg = self.Color_cabecera,
            height = 60,
        )
        self.pie.pack(side = tk.BOTTOM, fill = "both")
        self.pie.propagate(False)

        self.izquierda = tk.Frame(
            self,
            bg = self.Color_izquierda,
            width = 150,
        )
        self.izquierda.pack(side = tk.LEFT, fill = "both")
        self.izquierda.propagate(False)

        self.principal = tk.Frame(
            self,
            bg = self.Color_principal,
        )
        self.principal.pack(expand = True, fill = "both")
        self.principal.propagate(False)

    def newLabel(self, texto, where, aligment, size):
        self.label = tk.Label(where, text = texto, bg = where.cget("bg"), font = ("Elephant", size))
        self.label.pack(padx = 0, pady = 10, anchor = aligment, expand = True)
        return self.label
    
    def newImage(self, ruta, where):
        self.logo = tk.PhotoImage(file = ruta)
        self.logo.subsample(1, 1)
        self.label = tk.Label(where, image = self.logo, bg = where.cget("bg"))
        self.label.pack(padx = 3, pady = 3)
        return self.label
    
    """ def grafica(self):
        import matplotlib.pyplot as plt # type: ignore
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore

        fig, ax = plt.subplots()

        x = [1, 2, 3, 4, 5]
        y = [10, 20, 25, 35, 45]

        ax.plot(x, y)
        ax.set_title("Gráfica")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")

        canvas = FigureCanvasTkAgg(fig, master=self.principal)
        canvas.draw()
        canvas.get_tk_widget().pack()

        self.buttonGrafica.configure(text="Ocultar Gráfica", command=lambda:{
            self.principal.winfo_children()[1].destroy(),
            self.buttonGrafica.configure(text = "Mostrar Gráfica", command = self.grafica)
        })
    
    def botonGrafica(self, where):
        self.buttonGrafica = ttk.Button(where, text = "Mostrar Gráfica", command = self.grafica)
        self.buttonGrafica.pack(padx = 10, pady = 3, expand = True) """
    
    """ def enviarEmail(self):
        from correo import Correo
        email = self.principal

        usuariolbl = tk.Label(email, text = "Usuario: ", bg = self.principal.cget("bg"))
        usuariolbl.pack(padx = 10, pady = 10)
        usuarioet = ttk.Entry(email)
        usuarioet.pack(padx = 10, pady = 10)

        contrasenalbl = tk.Label(email, text = "Contraseña: ", bg = self.principal.cget("bg"))
        contrasenalbl.pack(padx = 10, pady = 10)
        contrasenaet = ttk.Entry(email, show = "*")
        contrasenaet.pack(padx = 10, pady = 10)

        destinolbl = tk.Label(email, text = "Destino: ", bg = self.principal.cget("bg"))
        destinolbl.pack(padx = 10, pady = 10)
        destinoet = ttk.Entry(email)
        destinoet.pack(padx = 10, pady = 10)

        asuntolbl = tk.Label(email, text = "Asunto: ", bg = self.principal.cget("bg"))
        asuntolbl.pack(padx = 10, pady = 10)
        asuntoet = ttk.Entry(email)
        asuntoet.pack(padx = 10, pady = 10)

        cuerpolbl = tk.Label(email, text = "Cuerpo: ", bg = self.principal.cget("bg"))
        cuerpolbl.pack(padx = 10, pady = 10)
        cuerpoet = tk.Entry(email)
        cuerpoet.pack(padx = 10, pady = 10)

        redactar = ttk.Button(self.principal, text = "Enviar", command = lambda:{
            Correo().enviarEmail(),
        })
        redactar.pack(padx = 10, pady = 10)
    
    def botonEmail(self, where):
        self.buttonEmail = ttk.Button(where, text = "Enviar Email", command = self.enviarEmail)
        self.buttonEmail.pack(padx = 10, pady = 3, expand = True) """
    
    
    