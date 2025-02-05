import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

Color_Cabecera = "#bfbfbf"
Color_Pie = "#bfbfbf"
Color_Principal = "#e2e2e2"
Color_Izquierda = "#d0d0d0"

class Ventana(tk.Tk):
    def __init__(self, ancho, alto, titulo, posx, posy):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
        self.titulo = titulo
        self.posx = posx
        self.posy = posy

        self.title(self.titulo)
        self.Color_principal = Color_Principal
        self.Color_pie = Color_Pie
        self.Color_izquierda = Color_Izquierda
        self.Color_cabecera = Color_Cabecera
        self.anchoPantalla = self.winfo_screenwidth()
        self.altoPantalla = self.winfo_screenheight()
        self.pos_x = (self.anchoPantalla // 2) - (self.ancho // 2)
        self.pos_y = (self.altoPantalla // 2) - (self.alto // 2)
        self.geometry(f"{self.ancho}x{self.alto}+{self.pos_x}+{self.pos_y}")
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
        self.label.pack(padx = 0, pady = 0, anchor = aligment, expand = True)
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
    """
    
    def botonGrafica(self, where):
        self.buttonGrafica = ttk.Button(where, text = "Gráfica Stock")
        self.buttonGrafica.pack(padx = 10, pady = 3, expand = True) 
    
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
    """

    def botonEmail(self, where):
        self.buttonEmail = ttk.Button(where, text = "Informe productos")
        self.buttonEmail.pack(padx = 10, pady = 3, expand = True)

    def aniadirProducto(self):
        producto = self.principal

        for i in range(6):
            producto.grid_rowconfigure(i, weight=1)
        producto.grid_columnconfigure(0, weight=1)
        producto.grid_columnconfigure(1, weight=1)

        def guardarProducto():

            if entryNArticulo.get() == "" or entryNombre.get() == "" or entryPrecio.get() == "" or entryStock.get() == "" or entryDescripcion.get() == "":
                messagebox.showerror("Error", "Por favor, rellene todos los campos")
            else:
                conn = mysql.connector.connect(user = "root", password = "1234", host = "localhost")
                print(conn)

                if conn.is_connected():
                    cursor = conn.cursor()
                    cursor.execute("CREATE DATABASE IF NOT EXISTS almacen")
                    cursor.execute("USE almacen")
                    cursor.execute("CREATE TABLE IF NOT EXISTS productos (nArticulo INT PRIMARY KEY, nombre VARCHAR(50), precio FLOAT, stock INT, descripcion VARCHAR(100));")
                    cursor.execute(f"SELECT COUNT(*) FROM productos WHERE nArticulo = {entryNArticulo.get()}")
                    
                    if cursor.fetchone()[0] > 0:
                        messagebox.showerror("Error", "El número de artículo ya existe en la base de datos")
                    else:
                        cursor.execute(f"INSERT INTO productos (nArticulo, nombre, precio, stock, descripcion) VALUES ({entryNArticulo.get()}, '{entryNombre.get()}', {entryPrecio.get()}, {entryStock.get()}, '{entryDescripcion.get()}');")
                        conn.commit()
                        messagebox.showinfo("Éxito", "Producto añadido correctamente")
                    cursor.close()

                conn.close()

        lblNArticulo = tk.Label(producto, text = "Número de artículo: ", bg = producto.cget("bg"))
        lblNArticulo.grid(row = 0, column = 0, padx = 0, pady = 10)

        entryNArticulo = ttk.Entry(producto)
        entryNArticulo.grid(row = 0, column = 1, padx = 0, pady = 10)

        lblNombre = tk.Label(producto, text = "Nombre: ", bg = producto.cget("bg"))
        lblNombre.grid(row = 1, column = 0, padx = 10, pady = 10)

        entryNombre = ttk.Entry(producto)
        entryNombre.grid(row = 1, column = 1, padx = 10, pady = 10)

        lblPrecio = tk.Label(producto, text = "Precio: ", bg = producto.cget("bg"))
        lblPrecio.grid(row = 2, column = 0, padx = 10, pady = 10)

        entryPrecio = ttk.Entry(producto)
        entryPrecio.grid(row = 2, column = 1, padx = 10, pady = 10)

        lblStock = tk.Label(producto, text = "Stock: ", bg = producto.cget("bg"))
        lblStock.grid(row = 3, column = 0, padx = 10, pady = 10)

        entryStock = ttk.Entry(producto)
        entryStock.grid(row = 3, column = 1, padx = 10, pady = 10)

        lblDescripcion = tk.Label(producto, text = "Descripción: ", bg = producto.cget("bg"))
        lblDescripcion.grid(row = 4, column = 0, padx = 10, pady = 10)

        entryDescripcion = ttk.Entry(producto)
        entryDescripcion.grid(row = 4, column = 1, padx = 10, pady = 10)

        btnGuardar = ttk.Button(producto, text = "Guardar", command = guardarProducto)
        btnGuardar.grid(row = 5, column = 0, padx = 10, pady = 10)

        btnCerrar = ttk.Button(producto, text = "Cerrar", command = lambda:{
            lblNArticulo.destroy(),
            entryNArticulo.destroy(),
            lblNombre.destroy(),
            entryNombre.destroy(),
            lblPrecio.destroy(),
            entryPrecio.destroy(),
            lblStock.destroy(),
            entryStock.destroy(),
            lblDescripcion.destroy(),
            entryDescripcion.destroy(),
            btnGuardar.destroy(),
            btnCerrar.destroy()
        })
        btnCerrar.grid(row = 5, column = 1, padx = 10, pady = 10)

    def botonProducto(self, where):
        self.buttonProducto = ttk.Button(where, text = "Añadir producto", command = self.aniadirProducto)
        self.buttonProducto.pack(padx = 10, pady = 3, expand = True)

    def botonCerrar(self, where):
        self.buttonCerrar = ttk.Button(where, text = "Cerrar programa", command = self.destroy)
        self.buttonCerrar.pack(padx = 10, pady = 3, expand = True)
    
    
    