original = {
    "Argentina": "Buenos Aires", 
    "Chile": "Santiago", 
    "Uruguay": "Montevideo"
}
invertido={}
for pais,capital in original.items():
    invertido[capital]=pais
print("ORGINAL:\n")
print(original)
print("\n INVERTIDO:\n")
print(invertido)