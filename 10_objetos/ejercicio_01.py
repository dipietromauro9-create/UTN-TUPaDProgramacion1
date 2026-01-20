class celda:
    def __init__(self,fila,columna,valor):
        self.fila=fila
        self.columna=columna
        self.valor=valor
    def __repr__(self):
        return f"Celda(fila={self.fila}, col={self.columna}, valor='{self.valor}')"
class matriz:
    def __init__(self):
        self.celdas=[]
    def agregar_celdas(self,fila:int,columna:int,valor:str):
        nueva_celda=celda(fila,columna,valor)
        self.celdas.append(nueva_celda)
    def __repr__(self):
        return f"Matriz(contenido={self.celdas})"
    def buscar_valor(self,fila_busc,columna_busc):
        for celda_actual in self.celdas:
            if celda_actual.fila==fila_busc and celda_actual.columna==columna_busc:
                return celda_actual.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"

mi_matriz=matriz()
while True:
    valor_usuario=str(input("Ingrese un valor (o 'FIN')"))
    if valor_usuario.lower()=="fin":
        break
    try:
        fila_usuario=int(input("Ingrese la fila de la celda: "))
        columna_usuario=int(input("Ingrese la columna de la celda: "))
        mi_matriz.agregar_celdas(fila_usuario,columna_usuario,valor_usuario)
        print(f"¡Celda ({fila_usuario}, {columna_usuario}, '{valor_usuario}') agregada con éxito!")
    except ValueError:
        print("¡ERROR! Ingrese un numero entero para las filas y columnas")
print("\n--- Contenido Final de la Matriz ---")
print(mi_matriz) 
print("---Busquedad de celdas---")
try:
    fila_busc=int(input("Imgrese la fila que desea buscar: "))
    columna_busc=int(input("Ingrese la columna que desea buscar: "))
    valor_encontrado=mi_matriz.buscar_valor(fila_busc,columna_busc)
    print(f"Resultado de la búsqueda ({fila_busc}, {columna_busc}): {valor_encontrado}")    
except ValueError:
    print("Error: Debía ingresar números enteros para la búsqueda")