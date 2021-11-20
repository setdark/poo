class Producto:
    def __init__(self,id,nombreProduc,precioProduc,stockProduc):
        self.id = id
        self.nombreProduc = nombreProduc
        self.precioProduc = precioProduc
        self.stockProduc = stockProduc

    def mostrarProducto(self):
        return "\nID      : " + str(self.id) +\
               "\nProducto: " + self.nombreProduc
    
          