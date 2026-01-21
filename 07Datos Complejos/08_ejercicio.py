inventario = {
    "Manzana": 50,
    "Banana": 20,
    "Naranja": 30
}
while True:
    try:
        print("-"*40)
        print("GESTION DE STOCK")
        print("-"*40)
        print("1.Consultar stock\n")
        print("2.Agregar unidades al stock\n")
        print("3.Agregar un nuevo producto\n")
        print("4.Salir\n")
        opcion=int(input())
        if opcion>4:
            print("Ingrese una opcion valida")
        elif opcion==4:
            break
        elif opcion==1:
            while True:
                    print("-"*40)
                    busqueda=str(input("Ingrese el producto que desea buscar o 'salir'\n"))
                    print("-"*40)
                    if busqueda.title() in inventario:
                        print(f"\nEl producto {busqueda.title()} tiene de stock: {inventario[busqueda.title()]}")
                    elif busqueda.lower()=="salir":
                        break
                    else:
                        print("El producto no existe")

        elif opcion==2:
            while True:
                producto=str(input("Ingrese el producto al que quiera agregarle stock o 'salir'\n"))
                if producto.title() in inventario:
                    agregar=int(input("ingrese la cantidad que desea agregar\n"))
                    inventario[producto.title()]+=agregar



                elif producto.lower()=="salir":
                    break
                else:
                    print("El producto no existe")

        elif opcion==3:
            while True:
                nuevo=str(input("Ingrese el producto que desea agregar o 'salir'\n"))
                if nuevo.title() in inventario:
                    print("El producto ya existe en el inventario")
                elif nuevo.lower()=="salir":
                    break
                else:
                    inventario[nuevo.title()]=int(input(f"Ingrese la cantidad de stock para {nuevo}\n"))
                    print("Producto agregado exitosamente\n")


    except ValueError:
        print("Ingrese una opcion valida")