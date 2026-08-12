arreglo1 = []
arreglo2 = [1, 2, True, "hola", 3.14]
print(arreglo2[1])
print (arreglo2)

for i in arreglo2:
    print(i, end=" ")


print()
for i in range(len(arreglo2)):
    print(arreglo2[i], end=" ")


    print()
    arreglo2.append("10")
    print(arreglo2)
    
    print()

    arreglo2.pop()

    nombres = []
    identificaciones = []

    n = int(input("cuantos datos desea ingresar:"))
    for i in range(n):
        print(f"Datos persona {i+1}")

        nombres.append(input("nombre:"))
        identificaciones.append(input("identificación:"))

for i in range(n):
    print(f"persona {i+1}")
    print(f"nombre: {nombres[i]}")
    print(f"identificación: {identificaciones[i]}")