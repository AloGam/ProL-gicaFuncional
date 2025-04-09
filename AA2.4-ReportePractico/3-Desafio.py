import tkinter as tk
from tkinter import messagebox, simpledialog
from functools import reduce

# Función para calcular el promedio de las valoraciones
def calcular_promedio(valoraciones):
    return reduce(lambda x, y: x + y, valoraciones) / len(valoraciones)

# Función para manejar el envío de la encuesta
def enviar_encuesta():
    aspectos = ["Actividades", "Herramientas", "Contenido", "Docencia", "Evaluación"]
    
    # Solicitar la cantidad de materias
    cantidad_materias = simpledialog.askinteger("Cantidad de Materias", "Ingrese la cantidad de materias:")
    if cantidad_materias is None or cantidad_materias <= 0:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un número válido de materias.")
        return

    # Ingresar nombres de las materias
    materias = []
    for i in range(cantidad_materias):
        materia = simpledialog.askstring("Materia", f"Ingrese el nombre de la materia {i + 1}:")
        if materia:
            materias.append(materia.strip())
        else:
            messagebox.showwarning("Advertencia", "Nombre de materia no ingresado. Por favor, completa todas las materias.")
            return

    resultados = {}

    for materia in materias:
        valoraciones = []
        for aspecto in aspectos:
            mensaje = (f"Calificaciones para la materia: {materia}\n"
                       f"Por favor, califica cada aspecto del 1 al 5.\n"
                       f"1 - Muy malo, 2 - Malo, 3 - Regular, 4 - Bueno, 5 - Excelente\n"
                       f"Califica el aspecto '{aspecto}' (1-5):")
            valor = simpledialog.askinteger("Calificación", mensaje, minvalue=1, maxvalue=5)
            if valor is not None:
                valoraciones.append(valor)
            else:
                messagebox.showwarning("Advertencia", "Calificación no ingresada. Por favor, completa todas las calificaciones.")
                return

        resultados[materia] = valoraciones

    # Calcular y mostrar resultados
    mostrar_resultados(resultados)

def mostrar_resultados(resultados):
    resultados_texto = ""
    for materia, valoraciones in resultados.items():
        promedio = calcular_promedio(valoraciones)
        total = sum(valoraciones)
        cantidad_valoraciones_bajas = len([v for v in valoraciones if v < 3])
        conteo_valoraciones = len(valoraciones)

        resultados_texto += (f"\nResultados de la materia: {materia}\n"
                             f"Promedio de valoraciones: {promedio:.2f}\n"
                             f"Total de valoraciones: {total:.2f}\n"
                             f"Cantidad de valoraciones bajas (menores a 3): {cantidad_valoraciones_bajas}\n"
                             f"Número total de valoraciones: {conteo_valoraciones}\n")

    messagebox.showinfo("Resultados de la Encuesta", resultados_texto)

# Crear la ventana principal
root = tk.Tk()
root.title("Encuesta de Evaluación")

# Botón para enviar la encuesta
btn_enviar = tk.Button(root, text="Iniciar Encuesta", command=enviar_encuesta)
btn_enviar.pack()

# Iniciar el bucle de la interfaz gráfica
root.mainloop()