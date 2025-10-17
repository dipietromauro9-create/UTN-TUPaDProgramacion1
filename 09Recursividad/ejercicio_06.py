def suma_digitos(n):
    if n==0:
        return 0
    else:
       return n+suma_digitos(n-1)
numero=int(input("Ingrese un numero: "))
print(suma_digitos(numero))