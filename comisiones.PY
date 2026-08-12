
n = int(input("Ingrese el número de vendedores (n): "))

for i in range(1, n + 1):
    print(f"--- Datos del Vendedor {i} ---")
    
    
    sueldo_base = float(input("Sueldo base: $"))
    venta1 = float(input("Monto de la venta 1: $"))
    venta2 = float(input("Monto de la venta 2: $"))
    venta3 = float(input("Monto de la venta 3: $"))
    
  
    total_ventas = venta1 + venta2 + venta3
    comisiones = total_ventas * 0.10  
    sueldo_total = sueldo_base + comisiones
    
   
    print(f"Ganancia por comisiones: ${comisiones:,.2f}")
    print(f"Sueldo total de la semana (Base + Comisiones): ${sueldo_total:,.2f}")