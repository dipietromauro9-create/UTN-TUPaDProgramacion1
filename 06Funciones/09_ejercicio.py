def celsius_a_fahrenheit(celsius):
    return celsius*1.8+32
celcius=float(input("Ingrese la temperatura en grados celcius: "))
fahrenheit=celsius_a_fahrenheit(celcius)
print(f"El equivalente de {celcius} grados celcius a grados fahrenheit es: {fahrenheit}")