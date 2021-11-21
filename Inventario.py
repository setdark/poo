from Producto import Producto
class Inventario:
    def __init__(self):
        self.listaProducto = []

        pro = Producto(1, "desatornillador", 800, 37)
        self.listaProducto.append(pro)
        pro = Producto(2, "martillo", 1500, 21)
        self.listaProducto.append(pro)
        pro = Producto(3, "llave francesa", 4000, 42)
        self.listaProducto.append(pro)
        pro = Producto(4, "corta carton", 500, 12)
        self.listaProducto.append(pro)
        pro = Producto(5, "alicate", 2000, 60)
        self.listaProducto.append(pro)
        pro = Producto(6, "caiman", 2500, 8)
        self.listaProducto.append(pro)
        pro = Producto(7, "pala", 6000, 20)
        self.listaProducto.append(pro)
        pro = Producto(8, "rastrillo", 5000, 21)
        self.listaProducto.append(pro)
        pro = Producto(9, "taladro", 15000, 23)
        self.listaProducto.append(pro)
        pro = Producto(10, "espatula", 850, 12)
        self.listaProducto.append(pro)
        pro = Producto(11, "brocha", 1000, 10)
        self.listaProducto.append(pro)

    def buscarProducto(self,id):
        for p in self.listaProducto:
            if id == p.id:
                return p
            else:
                None


    def descontarStock(self,id,stock):
        for p in self.listaProducto:
            if id == p.id:
                p.stockProduc = p.stockProduc - stock

    def cambiarPrecio(self,id,nuevoPrecio):
        for p in self.listaProducto:
            if id == p.id:
                p.precioProduc = nuevoPrecio
                print(p.mostrarProductoCompleto())