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

#Ejercicio 6#
from statistics import mode,median,mean
import random
numeros_aleatorios=[random.randint(1,100)for i in range(50)]
print(numeros_aleatorios)
print("El promedio de estos numeros es: ",mean(numeros_aleatorios))
print("El valor mas comun es:",mode(numeros_aleatorios))
print("La mediana es: ",median(numeros_aleatorios))
if mean(numeros_aleatorios)>median(numeros_aleatorios) and median(numeros_aleatorios)>mode(numeros_aleatorios):
    print("Hay sesgo positivo")
elif mean(numeros_aleatorios)<median(numeros_aleatorios) and median(numeros_aleatorios)<mode(numeros_aleatorios):
    print("Hay sesgo negativo")
elif mean(numeros_aleatorios)==median(numeros_aleatorios) and median(numeros_aleatorios)==mode(numeros_aleatorios):
    (print("sin sesgo"))

#Ejercicio 7#
texto=input("Ingrese un texto: ")
vocales="A,E,I,O,U,a,e,i,o,u"
if texto and texto[-1] in vocales:
    print(texto,"¡")
else:
    print(texto)

#Ejercicio 8#
nombre=input("Ingrese su nombre: ")
menu=input("Ingrese: 1. Si quiere su nombre en mayúsculas. 2. Si quiere su nombre en minúsculas.3. Si quiere su nombre con la primera letra mayúscula ")
if menu=="1":
    print(nombre.upper())
elif menu=="2":
    print(nombre.lower())
elif menu=="3":
    print(nombre.title())

#Ejercicio 9#
magnitud=int(input("Ingrese la magnitud del terremoto: "))
if magnitud<3:
    print("Muy leve (imperceptible).")
elif magnitud<4:
    print( "Leve (ligeramente perceptible).")
elif magnitud<5:
    print(" Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud<6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud<7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")