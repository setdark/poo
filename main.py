from Producto import Producto
from Boleta import Boleta

numeBoleta = 0

listaProducto = []

pro = Producto(1, "desatornillador", 800, 37)
listaProducto.append(pro)
pro = Producto(2, "martillo", 1500, 21)
listaProducto.append(pro)
pro = Producto(3, "llave francesa", 4000, 42)
listaProducto.append(pro)
pro = Producto(4, "corta carton", 500, 12)
listaProducto.append(pro)
pro = Producto(5, "alicate", 2000, 60)
listaProducto.append(pro)
pro = Producto(6, "caiman", 2500, 8)
listaProducto.append(pro)
pro = Producto(7, "pala", 6000, 20)
listaProducto.append(pro)
pro = Producto(8, "rastrillo", 5000, 21)
listaProducto.append(pro)
pro = Producto(9, "taladro", 15000, 23)
listaProducto.append(pro)
pro = Producto(10, "espatula", 850, 12)
listaProducto.append(pro)
pro = Producto(11, "brocha", 1000, 10)
listaProducto.append(pro)

ListaBoleta = []

def buscarPoducto(id,listaProducto):
    for p in listaProducto:
        if id == p.id:
            return p
        else:
            None
# def buscarProduc(id,listaProducto):
#     for p in listaProducto:
#         if id == p.id:
#             return p.nombreProduc
#         else:
#             return None
while True:
    print("\n1. Agregar Product"+\
          "\n2. Actualizar Precio"+\
          "\n3. Mostar Boleta"+\
          "\n4. salir")
    x = int(input("Ingrece una opcion: "))
    if x == 1:
        for i in listaProducto:
            print(i.mostrarProducto())
        ingreIdProduc = int(input("Ingrece el ID del producto a agregar: "))
        bus = buscarPoducto(ingreIdProduc,listaProducto)
        if bus == None:
            print("producto no encontrado")
        else:
            # numeBoleta += 1
            # indice = bus - 1
            # boleta = Boleta(numeBoleta,)
            




