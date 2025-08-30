#Ejercicio 1#
for i in range(0,101):
    print(i)
#Ejercicio 2#
numero=input("Ingrese un numero ")
digitos=len(numero)
print(f"La cantidad de digitos que tiene {numero} es {digitos}")
#Ejercicio 3#
x=int(input("Ingrese el primer numero "))
y=int(input("Ingrese el segundo numero "))
sumatoria=0
for i in range(x,y+1):
    sumatoria=sumatoria+i
print(f"El valor de la sumatoria entre estos 2 rangos es: {sumatoria}")
#Ejercicio 4#
sumatoria=0
num=1
while num!=0:
    num=int(input("Ingrese numero que quiere agregar a la secuencia: "))
    sumatoria=sumatoria+num
print(f"La sumatoria total es: {sumatoria}")
#Ejercicio 5#
import random
numero_aleatorio=random.randint(0,9)
print(numero_aleatorio)
cont=0
adivina=-1
while adivina!=numero_aleatorio:
    adivina=int(input("Adivina el numero: "))
    cont=cont+1
print(f"!Felicidades acertaste el numero¡ Cantidad de intentos {cont}")
#Ejercicio 6#
for i in range(100,-1,-2):
    print(i)
#Ejercicio 7#
num=int(input("Ingrese un numero entero positivo para el final de la secuencia "))
sumatoria=0
if num>0:
    for i in range(0,num+1):
        sumatoria=sumatoria+i
    print(f"La sumatoria total es: {sumatoria}")
else:
    print("Porfavor ingrese un numero positivo")