alumnos={}
for i in range(3):
    nombre=str(input("Ingrese el nombre del alumno:\n"))
    notas=[]
    for j in range(3):
        nota=notas.append(float(input("Ingrese 3 notas del alumno:\n")))
    tupla_1=tuple(notas)
    alumnos[nombre]=tupla_1
print("\nLas notas de los Alumnos son:")
print(alumnos)
print("\nEl proemdio de los alumnos es:")
for i in alumnos:
    print(f"\nEl proemdio de {i} es: {int(sum(alumnos[i])/3)}")