def es_primo(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 
def primos():
    numeros = []
    lista_numeros = int(input("Porfavor ingrese la cantidad de numeros que desea organizar: ")) 
    for i in range(lista_numeros):
        numero = int(input("Ingrese el valor " + str(i+1) + ": "))
        numeros.append(numero)
    for numero in numeros:
        if es_primo(numero):        
            print(f"el numero {numero} es primo")
        else:
            print(f"el numero {numero} NO es primo")
primos()