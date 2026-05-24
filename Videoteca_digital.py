# ==============================================================================
# UNAD - Fundamentos de Programación
# Evaluación Final POA - Fase 5
# Problema Seleccionado: Problema 4 - Videoteca Digital
# Estudiante: Jose Alirio Benavides
# Programa: Ingenieria electronica
# ==============================================================================

#-------------------------------------------------------------------------------
# 1. Módulo para calcular el conteo de títulos que cumplen con los criterios de año y calificación

def calcular_conteo_titulos(matriz_videos, calificacion_umbral, anio_limite):
    # Variable acumuladora clásica para el conteo
    contador = 0
    total_filas = len(matriz_videos)
    
    # Ciclo 'for' clásico para recorrer las filas
    for i in range(total_filas):
        anio_pelicula = matriz_videos[i][1]        # Columna 1: Año
        calificacion_pelicula = matriz_videos[i][2]  # Columna 2: Calificación
        
        
        if anio_pelicula >= anio_limite and calificacion_pelicula >= calificacion_umbral:
            contador = contador + 1
            
    return contador


videoteca = [
    ["Inception", 2010, 8.8, "Sci-Fi"],
    ["Interstellar", 2014, 8.7, "Sci-Fi"],
    ["Parasite", 2019, 8.5, "Thriller"],
    ["Dune: Part Two", 2024, 8.4, "Sci-Fi"],
    ["Oppenheimer", 2023, 8.2, "Drama"],
    ["Spider-Man: Into the Spider-Verse", 2018, 8.4, "Animación"],
    ["The Matrix", 1999, 8.7, "Sci-Fi"]
]

# Variable de control para mantener el menú activo
ejecutando = True

# Ciclo principal del menú
while ejecutando:
    print("\n=========================================")
    print("       SISTEMA DE VIDEOTECA DIGITAL      ")
    print("=========================================")
    print("1. Ver catálogo completo de películas")
    print("2. Evaluar compromiso (Filtrar películas)")
    print("3. Salir del programa")
    print("=========================================")
    
    # Capturamos la opción del usuario
    opcion = input("Seleccione una opción (1-2-3): ")
    print("-----------------------------------------")
    
    if opcion == "1":
        print("--- CATÁLOGO DE PELÍCULAS ---")
        # Recorremos la matriz para mostrar los datos actuales de forma ordenada
        for i in range(len(videoteca)):
            print("Título:", videoteca[i][0], "| Año:", videoteca[i][1], "| Nota:", videoteca[i][2], "| Género:", videoteca[i][3])
            
    elif opcion == "2":
        print("--- CONFIGURACIÓN DE FILTROS ---")
        
        # Validación para el Año Límite (Debe ser mayor a 0)
        solicitando_anio = True
        while solicitando_anio:
            limite_anio = int(input("Ingrese el año límite (ejemplo. 2015): "))
            if limite_anio > 0:
                solicitando_anio = False  # Rompe el bucle si es positivo
            else:
                print("Error: El año debe ser un número positivo mayor a cero.")
        
        # Validación para la Calificación Mínima (Debe ser mayor a 0)
        solicitando_nota = True
        while solicitando_nota:
            umbral_calificacion = float(input("Ingrese la calificación mínima (1-10): "))
            if umbral_calificacion > 0:
                solicitando_nota = False  # Rompe el bucle si es positivo
            else:
                print("Error: La calificación debe ser un número positivo mayor a cero.")
        
        print("-----------------------------------------")
        print("PELÍCULAS ENCONTRADAS QUE CUMPLEN:")
        print("-----------------------------------------")
        
        # Recorremos la matriz para mostrar cuáles cumplen individualmente
        for i in range(len(videoteca)):
            if videoteca[i][1] >= limite_anio and videoteca[i][2] >= umbral_calificacion:
                print("-", videoteca[i][0], "(Año:", videoteca[i][1], "| Nota:", videoteca[i][2], ")")
        
        # Llamamos al módulo para obtener el conteo total de títulos que cumplen ambos criterios
        resultado_final = calcular_conteo_titulos(videoteca, umbral_calificacion, limite_anio)
        
       
        print("-----------------------------------------")
        print("RESULTADO FINAL:")
        print("Total de títulos que cumplen los criterios:", resultado_final)
        
    elif opcion == "3":
        print("Saliendo del sistema... Gracias por usar el programa.")
        # Cambiamos la variable a False para romper el ciclo 'while'
        ejecutando = False
        
    else:
        print("Opción inválida. Por favor, intente de nuevo.")