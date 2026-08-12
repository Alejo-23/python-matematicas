
numBase = int(input("¿De qué número deseas ver la tabla de multiplicar?: "))

print(f"\n=== TABLA DEL {numBase} ===")

for i in range(1, 11):
    resultado = numBase * i
    print(f"{numBase} x {i} = {resultado}")


