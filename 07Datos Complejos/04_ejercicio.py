contactos={}
for i in range(5):
    nombres=input("Ingrese el nombre del contacto: ")
    telefono=input(f"Ingrese el numero de telefeno de {nombres}: ")
    contactos[nombres]=telefono
buscador=input("A quien deseas buscar ")
if buscador in contactos:
    print(f"El numero de telefono de {buscador} es: {contactos[buscador]}")
else:
    print("El contacto no existe ")
