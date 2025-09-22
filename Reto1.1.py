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