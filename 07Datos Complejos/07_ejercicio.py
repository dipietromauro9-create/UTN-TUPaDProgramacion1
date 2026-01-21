parcial_1 = {"Ana", "Luis", "Marta", "Pedro", "Juan"}
parcial_2 = {"Luis", "Elena", "Ana", "Jose", "Clara"}
aprobados_ambos=parcial_1 & parcial_2
aprobado_uno=parcial_1 ^ parcial_2
total_aprobados = parcial_1 | parcial_2
print(f"Alumnos que aprobaron los 2 parciales:\n{aprobados_ambos}")
print(f"Alumnos que aprobaron solo un parcial:\n{aprobado_uno}")
print(f"Total de estudiantes aprobados (al menos uno): {total_aprobados}")