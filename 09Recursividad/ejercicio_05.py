def  es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    # Si la primera y la última letra son distintas, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva quitando la primera y última letra
    return es_palindromo(palabra[1:-1])
print(es_palindromo("oso"))