class Producto:
    def __init__(self, nombre, precio, stock, nArticulo, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.nArticulo = nArticulo
        self.descripcion = descripcion

    def getNArticulo(self):
        return self.nArticulo
    
    def getStock(self):
        return self.stock
    
