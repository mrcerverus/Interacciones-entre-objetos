from tienda import Tienda, Restaurante, Supermercado, Farmacia


nombre_tienda = input("Ingrese el nombre de la tienda: ")
costo_delivery = float(input("Ingrese el costo de delivery: "))

tipo_tienda = input("Ingrese el tipo de tienda (Restaurante/Supermercado/Farmacia): ")
if tipo_tienda.lower() == "restaurante":
    tienda = Restaurante(nombre_tienda, costo_delivery)
elif tipo_tienda.lower() == "supermercado":
    tienda = Supermercado(nombre_tienda, costo_delivery)
elif tipo_tienda.lower() == "farmacia":
    tienda = Farmacia(nombre_tienda, costo_delivery)
else:
    print("Tipo de tienda no válido")


while True:
    opcion = input("Seleccione una opción:\n1. Ingresar producto\n2. Listar productos\n3. Realizar venta\n4. Salir\n")

    if opcion == "1":
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        if tipo_tienda != "Restaurante":
            stock_producto = int(input("Ingrese el stock del producto: "))
        else:
            stock_producto = 0    
        tienda.ingresar_producto(nombre_producto, precio_producto, stock_producto)
        print("Producto ingresado exitosamente.")

    elif opcion == "2":
        print("Listado de productos:")
        print(tienda.listar_productos())

    elif opcion == "3":
        nombre_producto = input("Ingrese el nombre del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))
        tienda.realizar_venta(nombre_producto, cantidad)

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

