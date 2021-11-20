def buscarPoducto(id,listaProducto):
    for p in listaProducto:
        if id == p.id:
            return p.nombreProduc
        else:
            None
def buscarStock(id,listaProducto):
    for p in listaProducto:
        if id == p.id:
            return p.stockProduc
        else:
            None
def buscarPrecio(id,listaProducto):
    for p in listaProducto:
        if id == p.id:
            return p.precioProduc
        else:
            None

# def generarBoleta(numBoleta,ListaBoleta):
#     for p in ListaBoleta:
#         if numBoleta == p.numeroBoleta:
#             boleta = p.mostrarBoleta()
#             print(boleta)
#         else: 
#             None