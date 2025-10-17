def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
    
#Mostrar todos los numeros enteros desde 1 hasta el num que indique el ususario#
num=int(input("Ingrese un numero: "))
for i in range(1,num+1):
    print(fact(i))