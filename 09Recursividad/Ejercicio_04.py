
def binario(x):
    if x<2:
        return str(x)
    else:
        return binario(x//2)+str(x%2)
num=int(input("Ingrese un numero: "))
print(binario(num))