texto=str(input("Ingrese un texto:\n"))
palabras=texto.lower().split()
palabras_unicas=set(palabras)
contador=0
recuento={}
for palabra in palabras:
    recuento[palabra]=palabras.count(palabra)
print("Palabras unicas:\n")
for i in palabras:
    print(i)
print("Recuento de palabras:\n")
for key,numero in recuento.items():
    print(f"{key}:{numero}")