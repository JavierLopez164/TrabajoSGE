import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PyPDF2 import PdfMerger

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


    # CONFIGURACION DE WIDGETS
    def clearFrame(self):
        for widget in self.principal.winfo_children():
            widget.destroy()

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
    

    # CREACIÓN DE GRÁFICA
    def grafica(self):
        import matplotlib.pyplot as plt # type: ignore
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore

        self.clearFrame()

        conn = mysql.connector.connect(user = "root", password = "1234", host = "localhost")
        print(conn)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("USE almacen")
            cursor.execute("SELECT stock FROM productos;")
            datosStock = cursor.fetchall()
            cursor.execute("SELECT nombre FROM productos;")
            datosNombre = cursor.fetchall()
            cursor.close()
        conn.close()

        fig, ax = plt.subplots()

        y = [stock[0] for stock in datosStock]
        x = [nombre[0] for nombre in datosNombre] 

        ax.plot(x, y)
        ax.set_title("Stock del almacén")
        ax.set_xlabel("Nombre del producto")
        ax.set_ylabel("Stock del producto") 

        canvas = FigureCanvasTkAgg(fig, master=self.principal)
        canvas.draw()
        canvas.get_tk_widget().pack()

        self.buttonGrafica.configure(text="Ocultar Gráfica", command=lambda:{
            self.clearFrame(),
            self.buttonGrafica.configure(text = "Mostrar Gráfica", command = self.grafica)
        })
    
    def botonGrafica(self, where):
        self.buttonGrafica = ttk.Button(where, text = "Gráfica Stock", command=self.grafica)
        self.buttonGrafica.pack(padx = 10, pady = 3, expand = True) 

    def generarPDF(self):
        from .pdf import PDF
        from datetime import datetime

        self.clearFrame()

        conn = mysql.connector.connect(user = "root", password = "1234", host = "localhost")

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("USE almacen")
            cursor.execute("SELECT * FROM productos;")
            productos = cursor.fetchall()
            cursor.close()
        conn.close()

        pdf_files = []
        for row in productos:
            info = {
                "nArticulo": row[0],
                "nombre": row[1],
                "precio": row[2],
                "stock": row[3],
                "descripcion": row[4],
                "fecha": datetime.now().strftime("%d/%m/%Y")
            }

            ruta_template = "./modelos/plantilla.html"
            ruta_css = "./estilos/estilos.css"
            ruta_salida = f'/mnt/c/Users/Raul/Desktop/TrabajoSGE/informes/Articulo{row[0]}.pdf'
            PDF(info).crearPDF(ruta_template, ruta_css, ruta_salida)
            pdf_files.append(ruta_salida)

        # Juntar los pdfs generados
        merger = PdfMerger()
        for pdf in pdf_files:
            merger.append(pdf)
        merger.write('/mnt/c/Users/Raul/Desktop/TrabajoSGE/informes/Informe_Productos.pdf')
        merger.close()

    # ENVÍO DE PDF POR CORREO
    def enviarEmail(self):
        from .correo import Correo

        self.clearFrame()

        email = self.principal
        asunto = "Informe de productos"
        cuerpo = "Adjunto encontrará el informe de productos generado."

        # Configurar el grid (añadimos 4 filas pero ponemos 4 más para que visualmente esté mejor)
        for i in range(8):
            email.grid_rowconfigure(i, weight=1)
        email.grid_columnconfigure(0, weight=1)
        email.grid_columnconfigure(1, weight=1)

        usuariolbl = tk.Label(email, text = "Usuario: ", bg = self.principal.cget("bg"))
        usuariolbl.grid(row = 0, column = 0, padx = 0, pady = 10)
        usuarioString = tk.StringVar()
        usuarioet = ttk.Entry(email, textvariable=usuarioString)
        usuarioet.grid(row = 0, column = 1, padx = 0, pady = 10)

        contrasenalbl = tk.Label(email, text = "Contraseña: ", bg = self.principal.cget("bg"))
        contrasenalbl.grid(row = 1, column = 0, padx = 10, pady = 10)
        contrasenaString = tk.StringVar()
        contrasenaet = ttk.Entry(email, textvariable=contrasenaString, show = "*")
        contrasenaet.grid(row = 1, column = 1, padx = 10, pady = 10)

        destinolbl = tk.Label(email, text = "Destino: ", bg = self.principal.cget("bg"))
        destinolbl.grid(row = 2, column = 0, padx = 10, pady = 10)
        destinoString = tk.StringVar()
        destinoet = ttk.Entry(email, textvariable=destinoString)
        destinoet.grid(row = 2, column = 1, padx = 10, pady = 10)

        

        redactar = ttk.Button(self.principal, text = "Enviar", command = lambda: {
            self.generarPDF(),
            Correo(
                usuarioString.get(), 
                contrasenaString.get(), 
                destinoString.get(), 
                asunto, 
                cuerpo, 
                adjunto='./informes/Informe_Productos.pdf'
            ).enviarEmail()
        })
        redactar.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10)

    def botonEmail(self, where):
        self.buttonEmail = ttk.Button(where, text = "Informe productos", command=self.enviarEmail)
        self.buttonEmail.pack(padx = 10, pady = 3, expand = True)


    # AÑADIR PRODUCTO A LA BASE DE DATOS
    def aniadirProducto(self):
        self.clearFrame()

        producto = self.principal

        # Configurar el grid (añadimos 8 filas pero ponemos 2 más para que visualmente esté mejor)
        for i in range(10):
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
                        entryNArticulo.delete(0, tk.END)
                        entryNombre.delete(0, tk.END)
                        entryPrecio.delete(0, tk.END)
                        entryStock.delete(0, tk.END)
                        entryDescripcion.delete(0, tk.END)
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
            self.clearFrame()
        })
        btnCerrar.grid(row = 5, column = 1, padx = 10, pady = 10)

    def botonProducto(self, where):
        self.buttonProducto = ttk.Button(where, text = "Añadir producto", command = self.aniadirProducto)
        self.buttonProducto.pack(padx = 10, pady = 3, expand = True)


    # CERRAR PROGRAMA
    def botonCerrar(self, where):
        self.buttonCerrar = ttk.Button(where, text = "Cerrar programa", command = self.destroy)
        self.buttonCerrar.pack(padx = 10, pady = 3, expand = True)

