def SumaCons():
    listanumero = []
    cantidadnumeros = int(input("Porfavor ingrese la cantidad de numeros que desea sumar consecutivamente: ")) 
    for i in range(cantidadnumeros):
        numero = int(input("Ingrese el valor " + str(i+1) + ": "))
        listanumero.append(numero)
    listanumero.sort()
    sumavaloresmax: int = sum(listanumero[-2:])
    print(f" la Suma mas alta posible es: {sumavaloresmax}")
SumaCons()