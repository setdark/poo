from Producto import Producto
from Boleta import Boleta
from funciones import *

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

while True:
    print("\n1. Agregar Product"+\
          "\n2. Actualizar Precio"+\
          "\n3. Mostar Boleta"+\
          "\n4. salir")
    x = int(input("Ingrece una opcion: "))
    if x == 1:
        for i in listaProducto:
            print(i.mostrarProducto())
        ingreIdProduc = int(input("\nIngrece el ID del producto a agregar: "))
        busProduc = buscarPoducto(ingreIdProduc,listaProducto)
        
        if busProduc == None:
            print("producto no tiene stock")
        else:
            buscarStock = buscarStock(ingreIdProduc,listaProducto)
            if buscarStock == None:
                print("Producto sin stock!!")
            else:
                a = int(input("\nEL producto tiene "+str(buscarStock)+" de stock cuanto se llevará: "))
                busPrecio = buscarPoducto(ingreIdProduc,listaProducto)
                numeBoleta += 1
                precio = busPrecio * a
                crearboleta = Boleta(numeBoleta, busProduc, a, precio)
                ListaBoleta.append(crearboleta)
                # print("\nSunumero de boleta es: "+str(numeBoleta))
    elif x == 3:
        print("BOLETA\n")
        for i in ListaBoleta:
            print(i.mostrarBoleta()) 

    elif x == 4:
        break


            




