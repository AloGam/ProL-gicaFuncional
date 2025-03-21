# Programa con función callback que realiza operaciones matemáticas.
def calcular(n1, n2, operacion):
    # Esta función toma dos números y una función (callback) como argumentos.
    # Ejecuta la función de operación con los dos números y devuelve el resultado.
    return operacion(n1, n2)

def suma(a, b):
    # Función que suma dos números.
    return a + b

def resta(a, b):
    # Función que resta el segundo número del primero.
    return a - b

def multiplicacion(a, b):
    # Función que multiplica dos números.
    return a * b

def division(a, b):
    # Función que divide el primer número por el segundo.
    # Maneja la división por cero.
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Uso de la función callback
num1 = 10
num2 = 5

# Llamadas a la función calcular con diferentes operaciones
resultado_suma = calcular(num1, num2, suma)
resultado_resta = calcular(num1, num2, resta)
resultado_multiplicacion = calcular(num1, num2, multiplicacion)
resultado_division = calcular(num1, num2, division)

# Imprimir los resultados de las operaciones
print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Multiplicación: {resultado_multiplicacion}")
print(f"División: {resultado_division}")

# Una función callback es una función que 
# se pasa como argumento a otra función.
# La función que recibe la función callback puede 
# ejecutarla o llamarla en un momento determinado.
