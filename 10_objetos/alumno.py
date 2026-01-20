from nota import Nota
class Alumno:
    def __init__(self,Nombre_completo,legajo):
        self.Nombre_completo=Nombre_completo
        self.legajo=legajo
        self.lista_notas=[]   
    def cargar_notas(self,catedra,nota_examen):
        nueva_nota=Nota(catedra,nota_examen)
        self.lista_notas.append(nueva_nota)
    def calcular_promedio(self):
        total_suma=0
        for elementos in self.lista_notas:
            total_suma+=elementos.nota_examen
        return total_suma/len(self.lista_notas)