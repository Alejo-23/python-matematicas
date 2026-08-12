n = int(input("Ingrese la cantidad de alumnos: "))
Hombres = 0
Mujeres = 0

for i in range(1, n + 1):
    print(f"--- Alumno {i} ---")
    
    while True:
        sexo = input("Ingrese el sexo del alumno (H/M): ").upper()
        if sexo in ["H", "M"]:
            if sexo == "H":
                Hombres += 1
            elif sexo == "M":
                Mujeres += 1
            break
        else:
            print("Error: Ingrese 'H' para hombre o 'M' para mujer. Intente de nuevo.")

print(f"--- Resultado Final ---")
print(f"Cantidad de hombres: {Hombres}")
print(f"Cantidad de mujeres: {Mujeres}")
