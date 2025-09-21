val1 = float(input("Porfavor ingrese el primer valor para la operacion que desea realizar "))
val2 = float(input("Porfavor ingrese el segundo valor para la operacion que desea realizar "))
operacion = str(input("Excelente, ahora ingrese la operacion que desea hacer (Suma, Resta, Multiplicacion, Division) "))

def suma(val1, val2):
    return val1 + val2 

def resta(val1, val2):
    return val1 - val2 

def multiplicacion(val1, val2):
    return val1 * val2

def division(val1, val2):
    return val1 / val2

if operacion == "+":
    print (suma(val1, val2))
elif operacion == "-":
    print (resta(val1, val2))
elif operacion == "*":
    print (multiplicacion(val1, val2))
elif operacion == "/":
    print (division(val1, val2))
else:
    print("Operacion invalida.")
