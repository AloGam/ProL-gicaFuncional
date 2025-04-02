Productos = ["Frijoles", 
             "Coca Cola", 
             "Zumo de Naranja", 
             "Café de Olla", 
             "Gorditas de Chicharrón", 
             "Huevos Motuleños"
             ]

#1 Lista de nombres ordenada alfabeticamente e imprimir 
#en cadena los nombres de los productos alfabeticamente
productos_ordenados = sorted(Productos)
productos_cadena = ", ".join(productos_ordenados)
print("Lista de productos ordenada: ", productos_cadena)

 #3 Lista ordenada a slug
productos_slug = list(map(lambda x: x.lower().replace(" ", "-"), productos_ordenados))
print("Lista de productos en slug: ", productos_slug)
