def contar_bloques(n):
    if n==1:
        return 1
    else:
        return n+contar_bloques(n-1)
num=int(input("Ingrese los bloques finales: "))
print(f"La cantidad de bloques usados es: {contar_bloques(num)}")