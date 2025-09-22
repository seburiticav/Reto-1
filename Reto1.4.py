def suma_consecutiva():
    lista_numero = []
    cantidad_numeros = int(
        input(
            "Por favor, ingrese la cantidad de números que desea sumar "
            "consecutivamente: "
        )
    )
    for i in range(cantidad_numeros):
        numero = int(
            input("Ingrese el valor " + str(i + 1) + ": ")
        )
        lista_numero.append(numero)
    lista_numero.sort()
    suma_valores_max = sum(lista_numero[-2:])
    print(f"La suma más alta posible es: {suma_valores_max}")


suma_consecutiva()