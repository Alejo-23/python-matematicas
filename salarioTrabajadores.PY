
n = int(input("Ingrese el número de obreros a procesar: "))

for i in range(1, n + 1):
    print(f"\n--- Obrero {i} ---")
    

    while True:
        horas = int(input("Ingrese las horas trabajadas esta semana: "))
        
        if horas >= 0:
            break 
        else:
            print("Error: Las horas trabajadas no pueden ser negativas. Intente de nuevo.")
    
  
    if horas <= 40:
     
        salario = horas * 20
    else:
        
        horasNormales = 40
        horasExtras = horas - 40
        
        salario = (horasNormales * 20) + (horasExtras * 25)
        
    print(f"El salario semanal del obrero {i} es de: ${salario:,.2f}")