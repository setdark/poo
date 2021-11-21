from Producto import Producto
from Boleta import Boleta
from Inventario import Inventario
inventario = Inventario()
numeBoleta = 0

ListaBoleta = []

while True:
    try:
        print("\n1. Agregar Product"+\
            "\n2. Actualizar Precio"+\
            "\n3. Mostar Boleta"+\
            "\n4. salir")
        x = int(input("Ingrece una opcion: "))
        if x == 1:
            for i in inventario.listaProducto:
                print(i.mostrarProducto())
            buscarId = int(input("\nIngrece el ID del producto a agregar: "))
            producto = inventario.buscarProducto(buscarId)
            if producto == None:
                print("\nEl producto no existe")
            else:

                if producto.stockProduc <= 0:
                    print("Producto sin stock!!")
                else:
                    while True:
                        cantidad = int(input("\nEL producto tiene "+str(producto.stockProduc)+" de stock cuanto se llevará: "))
                        if cantidad > producto.stockProduc:
                            print("\nNo hay suficiente stock para lo que se quiere llevar")
                        else:
                            numeBoleta += 1
                            precio = producto.precioProduc * cantidad
                            crearboleta = Boleta(numeBoleta, producto.nombreProduc, cantidad, precio)
                            ListaBoleta.append(crearboleta)
                            inventario.descontarStock(buscarId,cantidad)
                            print("\nEl producto fue agregado exitosamente!!")
                            break
        elif x == 2:
            for i in inventario.listaProducto:
                print(i.mostrarProducto())
            buscarId = int(input("\nIngrece el ID del producto del cual quiere cambiar el precio: "))
            producto = inventario.buscarProducto(buscarId)
            nuevoPrecio = int(input("\nEl precio de este articulo es $"+str(producto.precioProduc)+" cual va a ser su nuevo precio?: "))
            inventario.cambiarPrecio(buscarId, nuevoPrecio)
        elif x == 3:
            print("BOLETA\n")
            for i in ListaBoleta:
                print(i.mostrarBoleta()) 

        elif x == 4:
            break
        
        else:
            print("\nLa opcion ingresada es incorrecta!!")

    except ValueError:
            print("\nERROR!!, has ingresado una letra, por favor solo ingrese numeros")

            




