# =========================================================
# PROGRAMA DE CONTROL DE NOTAS Y EVALUACIÓN
# =========================================================

# 1. Definimos los datos de los estudiantes (Nombre y sus 3 notas)
estudiantes = [
    {"nombre": "Pía", "notas": [6.5, 5.8, 6.2]},
    {"nombre": "Carlos", "notas": [3.5, 4.0, 3.8]},
    {"nombre": "Ana", "notas": [7.0, 6.8, 6.5]},
    {"nombre": "Diego", "notas": [2.5, 3.0, 4.2]}
]

print("--- INICIANDO SISTEMA DE EVALUACIÓN ---")

# 2. Recorremos la lista de estudiantes para calcular sus situaciones
for alumno in estudiantes:
    nombre = alumno["nombre"]
    notas = alumno["notas"]
    
    # Calculamos el promedio sumando las notas y dividiendo por la cantidad
    promedio = sum(notas) / len(notas)
    
    # 3. Evaluamos la situación del alumno según su promedio (Escala chilena)
    if promedio >= 4.0:
        situacion = "APROBADO/A  "
    else:
        situacion = "REPROBADO/A "
        
    # 4. Mostramos el resultado final en pantalla formateando el promedio a 1 decimal
    print(f"Estudiante: {nombre:<8} | Promedio: {promedio:.1f} | Situación: {situacion}")

print("---------------------------------------")
print("¡Proceso de evaluación terminado con éxito!")
