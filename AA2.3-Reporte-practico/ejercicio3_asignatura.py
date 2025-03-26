asignaturas_viii = ["matematicas"]
nva_lista = [asignaturas_viii, "Programacion"]
print(asignaturas_viii)
print(nva_lista)

def agregar_asignatura(lista, asignatura):
    return lista + [asignatura]

print(agregar_asignatura(asignaturas_viii, input("Ingresar asignatura: ")))