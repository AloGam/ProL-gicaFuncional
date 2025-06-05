# Estado de sensores
humedad_suelo = 'baja'
temperatura = 30
hora = 20
prob_lluvia = False
# Función para verificar si es la hora adecuada para regar
def hora_adecuada():
    return hora < 10 or hora > 18
# Función principal para activar el riego
def activar_riego():
    return humedad_suelo == 'baja' and not prob_lluvia and hora_adecuada()
# Diagnóstico del sistema
def estado_riego():
    if activar_riego():
        print('Estado: Activado')
        return 'Activado'
    else:
        print('Estado: No activado')
        return 'No Activado'
# Regla para alerta de temperatura extrema
def alerta_calor():
    return temperatura >= 32
# Mensaje de alerta si se activa el riego por calor extremo
def recomendacion():
    if activar_riego():
        if alerta_calor():
            print('Alerta: Activado con alerta por calor extremo')
        else:
            print('Activado condiciones optimas')
    else:
        print('Alerta: Desactivado')
# Ejecución de la recomendación
estado_riego(), recomendacion()