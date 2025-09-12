def calcular_imc(peso,altura):
    return round(peso/(altura)**2,2)
peso=float(input("Ingrese su peso en Kg: "))
altura=float(input("Ingrese su altura en metros: "))
imc=calcular_imc(peso,altura)
print(f"Su indicice de masa corporal es: {imc}")    