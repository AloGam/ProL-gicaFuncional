def hacer_preguntas():
    preguntas = [
        "¿Te interesa la administración de redes y la seguridad informática?",
        "¿Te gusta trabajar con bases de datos y manejar grandes volúmenes de información?",
        "¿Disfrutas desarrollando aplicaciones y software?",
        "¿Te apasiona la programación y el hardware?",
        "¿Te interesa el modelado y la animación?",
        "¿Te gustaría gestionar proyectos y coordinar equipos?"
    ]
    
    ramas = {
        "Redes": 0,
        "Bases de Datos": 0,
        "Desarrollo de Software": 0,
        "Programación Hardware": 0,
        "Modelado 3D": 0,
        "Gestión de Proyectos de Software": 0
    }
    
    for pregunta in preguntas:
        print(pregunta)
        respuesta = input("Responde con 'si' o 'no': ").strip().lower()
        if respuesta == 'si':
            if pregunta == preguntas[0]:
                ramas["Redes"] += 1
            elif pregunta == preguntas[1]:
                ramas["Bases de Datos"] += 1
            elif pregunta == preguntas[2]:
                ramas["Desarrollo de Software"] += 1
            elif pregunta == preguntas[3]:
                ramas["Programación Hardware"] += 1
            elif pregunta == preguntas[4]:
                ramas["Modelado 3D"] += 1
            elif pregunta == preguntas[5]:
                ramas["Gestión de Proyectos de Software"] += 1
    
    return ramas

def calcular_rama(ramas):
    rama_recomendada = max(ramas, key=ramas.get)
    return rama_recomendada

def main():
    print("Bienvenido al sombrero seleccionador de ISC")
    ramas = hacer_preguntas()
    rama_recomendada = calcular_rama(ramas)
    print(f"La rama de sistemas computacionales más recomendable para ti es: {rama_recomendada}")

if __name__ == "__main__":
    main()