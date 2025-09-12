def opereaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    mult=a*b
    divicion=a/b
    return(suma,resta,mult,divicion)
num1=int(input("Ingrese el primer numero "))
num2=int(input("Ingrese el segundo numero "))
resutlados=opereaciones_basicas(num1,num2)
print(f"La suma de {num1} y {num2} es: {resutlados[0]}")
print(f"La resta de {num1} y {num2} es: {resutlados[1]}")
print(f"La multiplicacion de {num1} y {num2} es: {resutlados[2]}")
print(f"La division de {num1} y {num2} es: {resutlados[3]}")