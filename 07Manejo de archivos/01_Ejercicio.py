with open("productos.txt","w")as archivo:
    archivo.write("Nombre:Lapicera,Precio:1200,Cantidad:30\n")
    archivo.write("Nombre:goma,Precio:800,Cantidad:50\n")
    archivo.write("Nombre:Lapiz,Precio:500,Cantidad:40\n")
productos=[]
with open("productos.txt","r")as archivo:
    for linea in archivo:
        linea=linea.strip()
        palabras=linea.split(",")
        nombre=palabras[0].split(":")[1]
        precio=palabras[1].split(":")[1]
        cantidad=palabras[2].split(":")[1]
        producto={
            "Nombre":nombre,
            "Precio":precio,
            "Cantidad":cantidad
        }
        productos.append(producto)
        print(f"Producto:{nombre}|Precio:{precio}|Cantidad:{cantidad}")
with open("productos.txt","a")as archivo:
    while True:
        nuevo=(str(input("Ingrese nuevo producto o 'salir' : ")))
        if nuevo.lower()=="salir":
            break
        try:
            palabras=nuevo.strip().split(",")
            nombre=palabras[0].split(":")[1]
            precio=int(palabras[1].split(":")[1])
            cantidad=int(palabras[2].split(":")[1])
            archivo.write(nuevo+"\n")  
            productos.append({
            "Nombre":nombre,
            "Precio":precio,
            "Cantidad":cantidad
            })  
        except (IndexError,ValueError):
            print("Ingrese el formato adecuado")
with open("productos.txt","r")as archivo:
    for linea in archivo:
        linea=linea.strip()
        palabras=linea.split(",")
        nombre=palabras[0].split(":")[1]
        precio=palabras[1].split(":")[1]
        cantidad=palabras[2].split(":")[1]
        print(f"Producto:{nombre}|Precio:{precio}|Cantidad:{cantidad}")
while True:
        buscador=str(input("Ingrese el producto que desea buscar o salir: "))
        if buscador.lower()=="salir":
            break
        elemento_encontrado=None
        for elementos in productos:
            if elementos['Nombre'].lower()==buscador.lower():
                elemento_encontrado=elementos
                print(elementos)
                break
        if elemento_encontrado==None:
            print("El Producto no se encuentra disponible")
with open("productos.txt","w") as archivo:
    for p in productos:
        archivo.write(str(p)+"\n")