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
