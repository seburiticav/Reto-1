def Anagramas():
    listapalabras = []
    letras_por_palabra = []
    cantidadpalabras = int(input("Porfavor ingrese la cantidad de palabras que desea añadir a la lista: ")) 
    for i in range(cantidadpalabras):
        palabra = str(input("Ingresela palabra " + str(i+1) + ": "))
        listapalabras.append(palabra)
        letras_por_palabra.append(sorted(list(palabra)))
    for i in range((len(letras_por_palabra))):
        for j in range (i +1, len(letras_por_palabra)):
            if letras_por_palabra[i] == letras_por_palabra[j]:
                print(f"Las palabras anagramas son {listapalabras[i]} y {listapalabras[j]}")
Anagramas()