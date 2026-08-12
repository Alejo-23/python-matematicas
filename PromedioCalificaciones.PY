
n = int(input("Ingrese la cantidad de alumnos en el grupo: "))

sumaCalificaciones = 0


for i in range(1, n + 1):
    print(f"\n--- Alumno {i} ---")
    
  
    while True:
        calificacion = float(input("Ingrese la calificación (0.0 - 10.0): "))
        
        if 0 <= calificacion <= 10:
            break 
        else:
            print("Error: La calificación debe estar en el rango de 0 a 10. Intente de nuevo.")
            

    sumaCalificaciones += calificacion


promedio = sumaCalificaciones / n



print(f"       RESULTADO DEL GRUPO           ")

print(f"Total de alumnos evaluados: {n}")
print(f"Suma de todas las notas: {sumaCalificaciones:.2f}")
print(f"Promedio general del grupo: {promedio:.2f}")
