def calcular_area(radio):
    return 3.1415*radio ** 2
def calcular_perimetro(radio):
    return 2*3.1415*radio
#Principal#
radio=float(input("Ingrese el radio del circulo: "))
print(f"El area del circulo es: {calcular_area(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro(radio)}")