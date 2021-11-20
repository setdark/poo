class Boleta:
    def __init__(self,numeroBoleta,articulo,cantidad,precioArticulo):
        self.numeroBoleta = numeroBoleta
        self.articulo = articulo
        self.cantidad = cantidad
        self.precioArticulo = precioArticulo

    def mostrarBoleta(self):
        return "\nNum Boleta     : " + str(self.id) +\
               "\nArticulo: " + self.nombreProduc +\
               "\nCantidad  : " + str(self.precioProduc) +\
               "\nPrecio   : " + str(self.stockProduc)

