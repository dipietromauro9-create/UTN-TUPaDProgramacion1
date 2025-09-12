def calcular_promedio(a, b, c):
    return round((a+b+c)/3,2)
num1=float(input("Ingrese el primer numero a promediar: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))
promedio=calcular_promedio(num1,num2,num3)
print(f"El proemedio de {num1}, {num2} y {num3} es: {promedio}")