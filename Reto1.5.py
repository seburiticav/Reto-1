def anagramas():
    lista_palabras = []
    letras_por_palabra = []
    cantidad_palabras = int(
        input(
            "Por favor, ingrese la cantidad de palabras que desea añadir a la lista: "
        )
    )
    for i in range(cantidad_palabras):
        palabra = str(
            input("Ingrese la palabra " + str(i + 1) + ": ")
        )
        lista_palabras.append(palabra)
        letras_por_palabra.append(sorted(list(palabra)))
    for i in range(len(letras_por_palabra)):
        for j in range(i + 1, len(letras_por_palabra)):
            if letras_por_palabra[i] == letras_por_palabra[j]:
                print(
                    f"Las palabras anagramas son {lista_palabras[i]} y {lista_palabras[j]}"
                )


anagramas()