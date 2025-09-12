"""#Ejercicio 1#
valorDecimal=float(input("Ingrese un valor decimal: "))
print(valorDecimal)
num=int(valorDecimal)
print(num)"""
#Ejercicio 19: #
"""Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un
atributo de nombre operación.
Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:
sumarNumeros()
restarNumeros()
multiplicarNumeros()
dividirNumeros()
El quinto método será el siguiente:
aplicarOperacion(operacion)
Cree una clase Calculo que contenga un método main, donde cree una instancia de la
clase OperacionMatematica, asigne 2 valores para las variables de la instancia y
ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “-
”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las
operaciones. """
class Operacion_matematicas:
    def __init__(self,valor1,valor2):
        self.valor1=valor1
        self.valor2=valor2

    
    def sumarNumeros(self):
       suma= self.valor1+self.valor2
       print(f"La suma de {self.valor1} y {self.valor2} es {suma}")
    
    
    def restarNumeros(self):
        resta= self.valor1-self.valor2
        print(f"La resta de {self.valor1} y {self.valor2} es {resta}")
        
    def multiplicarNumeros(self):
        multiplicacion= self.valor1*self.valor2
        print(f"La multiplicacion de {self.valor1} y {self.valor2} es {multiplicacion}")

    def dividirNumeros(self):
        division= self.valor1/self.valor2
        print(f"La division de {self.valor1} y {self.valor2} es {division}")

    def aplicarOperaciones(self, operacion):
        if operacion=="+":
            self.sumarNumeros()
        elif operacion=="-":
            self.restarNumeros()
        elif operacion=="*":
            self.multiplicarNumeros()
        elif operacion=="/":
            self.dividirNumeros()
        
class Calculo: 

    def main(self):
        operacion = Operacion_matematicas(10,5)
        operacion.aplicarOperaciones("+")
        operacion.aplicarOperaciones("-")
        operacion.aplicarOperaciones("*")
        operacion.aplicarOperaciones("/")

laconchadetumadre = Calculo()
laconchadetumadre.main()