# Reto #01 de POO
Entrega del primer reto planteado por Felipe Gonzales Roldan para programacion orientada objetos en la universidad nacional de colombia
## 1.1
Se le pide al usuario que ingrese 2 valores numericos y se plantea una funcion con los 2 valores ingresados como variables que ejecuta la formula de la operacion que el usuario pide que se realice y se plantea un if - elif - else que hace que si no se ingresa un simbolo de operacion valido imprima un mensaje que diga "operacion invalida"
```python
def suma(val1, val2):
    return val1 + val2


def resta(val1, val2):
    return val1 - val2


def multiplicacion(val1, val2):
    return val1 * val2


def division(val1, val2):
    return val1 / val2


val1 = float(
    input(
        "Por favor, ingrese el primer valor para la operación que desea realizar: "
    )
)
val2 = float(
    input(
        "Por favor, ingrese el segundo valor para la operación que desea realizar: "
    )
)
operacion = str(
    input(
        "Excelente, ahora ingrese la operación que desea hacer "
        "(+, -, *, /): "
    )
)

if operacion == "+":
    print(suma(val1, val2))
elif operacion == "-":
    print(resta(val1, val2))
elif operacion == "*":
    print(multiplicacion(val1, val2))
elif operacion == "/":
    print(division(val1, val2))
else:
    print("Operación inválida.")
```
## 1.2
Se define la funcion palindromo y la funcion comprobacion, utilizando la variable palabra se plantea que "palabra_invertida" utiliza reversed para invertir la cadena por caracteres separados y join para unir estos valores en un string completo, despues de aplicado esto en la funcion comprobacion se plantea un if que comprueba si el resultado de palabra_invertida es igual a la variable palabra y si es asi imprime un mensaje consecuente a esto, igualmente si el resultado no es igual imprime un mensaje acorde
```python
def palindromo(palabra):
    palabra_invertida = ''.join(reversed(palabra))
    if palabra == palabra_invertida:
        return "La palabra es un palíndromo."
    else:
        return "La palabra NO es un palíndromo."


def comprobacion(palabra):
    if not palabra.isalpha() or len(palabra) < 3:
        return "La palabra no es válida."
    else:
        return palindromo(palabra)


palabra = str(
    input(
        "Por favor, ingrese una palabra que tenga más de 2 caracteres, "
        "que no posea valores numéricos y que no posea símbolos: "
    )
)
print(comprobacion(palabra))
```
## 1.3
se crea la funcion es_primo que mediante la formula planteada comprueba si un valor n es primo o no y despues se crea la funcion primos, la cual mediante una lista almacena todos los valores ingresados por el usuario y llama a la funcion es_primo para comprobar que valores de toda la lista cumplen la condicion y cuales no
```python
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primos():
    numeros = []
    lista_numeros = int(
        input(
            "Por favor, ingrese la cantidad de números que desea organizar: "
        )
    )
    for i in range(lista_numeros):
        numero = int(
            input("Ingrese el valor " + str(i + 1) + ": ")
        )
        numeros.append(numero)
    for numero in numeros:
        if es_primo(numero):
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} NO es primo.")


primos()
```
## 1.4
se crea la funcion suma_consecutiva que almacena los valores ingresados en una lista, y usando .sort los organiza de menor a mayor, despues de esto, usando slicing suma los 2 ultimos valores de la lista (que seran los valores mas altos, por tanto la suma posible mas alta)
```python
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
```
## 1.5
Se plantean 2 listas (ademas de la funcion que ejecuta el programa), una que almacena las palabras que quiera ingresar el usuario y otra que separa cada palabra en letras separadas, despues se añaden las letras de cada palabra ordenadas alfabeticamente en la lista letras_por_palabra y finalmente se le pide al programa que recorra 2 veces (i y j) la lista con todas las palabras separadas y si existen 2 palabras que posean las mismas letras las imprima
```python
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
```
