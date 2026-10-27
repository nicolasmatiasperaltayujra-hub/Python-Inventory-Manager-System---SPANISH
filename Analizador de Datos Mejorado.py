inventario = {
    "Laptop": 800.00,
    "Mouse": 25.00,
    "Teclado": 45.00,
    "Monitor": 250.00,
    "Audífonos": 15.00
}

def calcular_promedio(productos):
    total = sum(productos.values())
    promedio = total / len(productos) if productos else 0
    return promedio

def encontrar_mas_caro(productos):
    producto_mas_caro = None
    precio_mas_alto = 0
    for producto in productos:
        if productos[producto] > precio_mas_alto:
            precio_mas_alto = productos[producto]
            producto_mas_caro = producto
    return producto_mas_caro, precio_mas_alto

def encontrar_mas_barato(productos):
    producto_mas_barato = None
    precio_mas_bajo = float('inf')
    for producto in productos:
        if productos[producto] < precio_mas_bajo:
            precio_mas_bajo = productos[producto]
            producto_mas_barato = producto
    return producto_mas_barato, precio_mas_bajo
while True:
    try:
        print("\nOpciones:")
        print("1. Calcular promedio de precios")
        print("2. Encontrar producto más caro")
        print("3. Encontrar producto más barato")
        print("4. Agregar un producto al inventario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            promedio = calcular_promedio(inventario)
            print(f"El precio promedio de los productos es: ${promedio:.2f}")
        elif opcion == "2":
            producto_mas_caro, precio_mas_alto = encontrar_mas_caro(inventario)
            print(f"El producto más caro es '{producto_mas_caro}' con un precio de ${precio_mas_alto:.2f}")
        elif opcion == "3":
            producto_mas_barato, precio_mas_bajo = encontrar_mas_barato(inventario)
            print(f"El producto más barato es '{producto_mas_barato}' con un precio de ${precio_mas_bajo:.2f}")
        elif opcion == "4":
            try:
                nombre_producto = input("Ingrese el nombre del producto: ")
                precio_producto = float(input("Ingrese el precio del producto: "))
                inventario[nombre_producto] = precio_producto
                print(f"Producto agregado al inventario: {nombre_producto} - ${precio_producto:.2f}")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número válido.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido.")
print(inventario)