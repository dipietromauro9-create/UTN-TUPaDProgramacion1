def potencia(b,e):
    if e==0:
        return 1
    else:
        return b*potencia(b,e-1)
base=int(input("Ingrese la base "))
exp=int(input("Ingrese el exponenete "))
print(potencia(base,exp))