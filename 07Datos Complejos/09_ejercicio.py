agenda = {
    ("Lunes", "09:00"): "Reunión de equipo",
    ("Martes", "14:30"): "Turno médico",
    ("Viernes", "18:00"): "Clase de Python"
}
print("-"*40)
print("CONSULTA DE AGENDA")
print("-"*40)
while True:
    dia=str(input("Ingrese el dia que quiere consultar en la agenda o 'salir'\n"))
    if dia.lower()=="salir":
        break
    hora=str(input("Ingrese la hora\n"))
    Dia=dia.title()
    consulta=(Dia,hora)
    if consulta in agenda:
        print(f"Usted tiene agendado el dia {Dia} a las {hora}: {agenda[consulta]}")
    else:
        print("No tiene nada agendado")
