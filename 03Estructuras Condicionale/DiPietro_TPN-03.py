#Ejercicio 1:#
edad=int(input("Ingrese su edad"))
if edad>=18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

#Ejercicio 2:#
nota=int(input("Ingrese su nota: "))
if nota>=6:
    print("Usted esta aprobado")
else:
    print("Usted esta desaprobado")

#Ejercicio 3:#
numpar=int(input("Ingrese un numero par "))
if numpar%2==0:
    print("Usted ingreso un numero par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4:#
edad4=int(input("Ingrese su edad "))
if edad4<12:
    print("Pertenece a la categoría niño/a")
elif edad4<18:
    print("Pertenece a la categoría adolecente")
elif edad4<30:
    print("Pertenece a la categoría adulto/a joven")
else:
    print("Pertenece a la categoría adulto/a")

#Ejercicio 5#
contraseña=input("Ingrese una contraseña entre 8 y 14 caracteres ")
if contraseña>=8 and contraseña<=18:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")