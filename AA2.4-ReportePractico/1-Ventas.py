from functools import reduce

ventas=[1500, 2500, 3200, 4500, 6000, 1200, 8000]

#1 promedio de ventas 
promedio = reduce(lambda x, y: x + y, ventas) / len(ventas) if ventas else 0
print("El promedio de ventas en pesos mexicanos es: ", round(promedio, 2))

#2 pesos a dolares
dolares = 20.46
pesos_dolares = list(map(lambda venta: round(venta / dolares, 2), ventas))   
print("Las ventas de la seman en dolares: ", pesos_dolares)

#3 filtrar ventas mayores a 150 dolares
ventas_mayores = list(filter(lambda venta: venta > 150, pesos_dolares))
print("Las ventas en dólares mayores a 150: ", ventas_mayores)

#4 total de ventas filtradas
ventas_filtro = reduce(lambda x, y: x + y, ventas_mayores) if ventas_mayores else 0
print("La suma total de las ventas en dólares mayores a 150: ", round(ventas_filtro, 2))