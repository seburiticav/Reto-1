palabra = str(input("Porfavor ingrese una palabra que tenga mas de 2 caracteres, que no posea valores numericos y que no posea simbolos: ")) 
def palindromo(palabra):
    palabra_invertida = ''.join(reversed(palabra))
    if palabra == palabra_invertida:
        return "La palabra es un palindromo"
    else:
        return "La palabra NO es un palindromo"
def comprobacion(palabra):
    if not palabra.isalpha() or len(palabra) < 3:
        return "La palabra no es valida"
    else:
        return palindromo(palabra)
print(comprobacion(palabra))