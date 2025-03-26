asignaturas_viii = ["matematicas"]
def asignaturas(lista):
    asig_nueva = input("Ingresar asignatura o 'exit' para salir: ")
    if asig_nueva == "exit":
        return lista
    return asignaturas(lista + [asig_nueva])

print(asignaturas(asignaturas_viii))