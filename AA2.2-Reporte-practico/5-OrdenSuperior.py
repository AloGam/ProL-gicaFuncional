# Programa de orden superior que aplica una función a un valor.
def aplicar_funcion(funcion, valor):
    return funcion(valor)

def elevar_al_cuadrado(x):
    return x ** 2
# El programa es de orden superior porque la función aplicar_funcion
# recibe como argumento una función y un valor, y retorna un valor. 
resultado = aplicar_funcion(elevar_al_cuadrado, 4) 
# Llamamos a la función con la función elevar_al_cuadrado y el valor 4
print(f"El resultado de elevar al cuadrado es: {resultado}")
