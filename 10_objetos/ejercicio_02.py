from alumno import Alumno
def main():
    alumnos=[]
    print("SISTEMA DE CARGA DE ALUMNOS")
    while True:
        Nombre_alumno=input("Ingrese el Nombre del alumno o 'FIN'")
        if Nombre_alumno.lower()=="fin":
            break
        try:
            legajo_alumno=int(input(f"Ingrese el legajo de {Nombre_alumno} : "))
        except ValueError:
            print("Ingrese numero para el legajo")
            continue
        nuevo_alumno=Alumno(Nombre_completo=Nombre_alumno,legajo=legajo_alumno)
        print("SISTEMA DE CARGA DE NOTAS")
        while True:
            catedra_nota=input("Ingrese la catedra o 'FIN")
            if catedra_nota.lower()=="fin":
                if not nuevo_alumno.lista_notas:
                    print("¡ERROR! Debe ingresar al menos UNA nota para este alumno.")
                    continue
                else:
                    break
            try:
                nota_examen=float(input(f"Ingrese la nota de {catedra_nota} "))
            except ValueError:
                print("Debe de ingresar un numero para la nota")
                continue
            nuevo_alumno.cargar_notas(catedra_nota,nota_examen)
            print(f"Nota de {catedra_nota} ({nota_examen}) agregada con éxito.")
        alumnos.append(nuevo_alumno)
    print("INFORMACION FINAL CARGADA")
    if not alumnos:
        print("Ningun alumno fue cargado")
    else:
        for alumno in alumnos:
            print("---------------------------------")
            print(f"Legajo: {alumno.legajo}")
            print(f"Nombre: {alumno.Nombre_completo}")
            print("Notas:")
            for nota in alumno.lista_notas:
                print(f"-{nota.catedra}:{nota.nota_examen}")
            promedio=alumno.calcular_promedio()
            print(f"**Promedio: {promedio:.2f}**")
if __name__ == "__main__":
    main()