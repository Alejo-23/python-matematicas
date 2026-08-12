
cantidadAlumnos = int(input("Ingrese la cantidad total de alumnos: "))


sumaEdadesHombres = 0
cuentaHombres = 0

sumaEdadesMujeres = 0
cuentaMujeres = 0

sumaEdadesGrupo = 0 


for i in range(1, cantidadAlumnos + 1):
    print(f"\n--- Alumno {i} ---")
    
    
    while True:
        sexoAlumno = input("Ingrese el sexo del alumno (H/M): ").upper()
        if sexoAlumno in ["H", "M"]:
            break
        else:
            print("Error: Ingrese 'H' para hombre o 'M' para mujer.")
            
 
    while True:
        edadAlumno = int(input("Ingrese la edad del alumno: "))
        if edadAlumno > 0:
            break
        else:
            print("Error: La edad debe ser un número positivo.")
            
   
    sumaEdadesGrupo += edadAlumno
    
    if sexoAlumno == "H":
        sumaEdadesHombres += edadAlumno
        cuentaHombres += 1
    else:
        sumaEdadesMujeres += edadAlumno
        cuentaMujeres += 1



if cuentaHombres > 0:
    promedioHombres = sumaEdadesHombres / cuentaHombres
else:
    promedioHombres = 0


if cuentaMujeres > 0:
    promedioMujeres = sumaEdadesMujeres / cuentaMujeres
else:
    promedioMujeres = 0


if cantidadAlumnos > 0:
    promedioGeneral = sumaEdadesGrupo / cantidadAlumnos
else:
    promedioGeneral = 0



print(f"        REPORTE DE EDADES            ")

print(f"Promedio de edad de HOMBRES: {promedioHombres:.1f} años (Total: {cuentaHombres})")
print(f"Promedio de edad de MUJERES: {promedioMujeres:.1f} años (Total: {cuentaMujeres})")
print(f"-------------------------------------")
print(f"PROMEDIO GENERAL DEL GRUPO : {promedioGeneral:.1f} años (Total: {cantidadAlumnos})")





