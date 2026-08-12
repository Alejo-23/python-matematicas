
n = int(input("Ingrese la cantidad de autos que entran a la ciudad: "))

amarilla = 0
rosa = 0
roja = 0
verde = 0
azul = 0

for i in range(1, n + 1):
    print(f"\n--- Vehículo {i} ---")
    
  
    while True:
        digito_str = input("Ingrese el último dígito de la placa (0-9): ")
        
       
        if len(digito_str) == 1 and digito_str.isdigit():
            digito = int(digito_str)
            break 
        else:
            print("Error: Debe ingresar un único dígito numérico entre 0 y 9.")
            
 
    if digito == 1 or digito == 2:
        amarilla += 1
    elif digito == 3 or digito == 4:
        rosa += 1
    elif digito == 5 or digito == 6:
        roja += 1
    elif digito == 7 or digito == 8:
        verde += 1
    elif digito == 9 or digito == 0:
        azul += 1

print(f"       REPORTE DE CALCOMANÍAS        ")
print(f"Calcomanías Amarillas (1 o 2): {amarilla}")
print(f"Calcomanías Rosas     (3 o 4): {rosa}")
print(f"Calcomanías Rojas     (5 o 6): {roja}")
print(f"Calcomanías Verdes    (7 o 8): {verde}")
print(f"Calcomanías Azules    (9 o 0): {azul}")
print(f"-------------------------------------")
print(f"Total de autos procesados: {n}")