class Boleta:
    def __init__(self,numeroBoleta,articulo,cantidad,precioArticulo):
        self.numeroBoleta = numeroBoleta
        self.articulo = articulo
        self.cantidad = cantidad
        self.precioArticulo = precioArticulo

    def mostrarBoleta(self):
        return "\nNum Boleta     : " + str(self.numeroBoleta) +\
               "\nArticulo: " + self.articulo +\
               "\nCantidad  : " + str(self.cantidad) +\
               "\nPrecio   : " + str(self.precioArticulo)

