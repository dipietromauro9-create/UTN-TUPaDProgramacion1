def segundos_a_horas(segundos):
    return segundos/3600
segundos=int(input("Ingrese la cantidad de segundos que quiera pasar a horas: "))
print(f"Los {segundos} segundos, son igual a {int(segundos_a_horas(segundos))} horas")