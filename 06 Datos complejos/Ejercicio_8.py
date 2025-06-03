''''Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe. '''


stock_productos = {'fideos': 50, 'salsa': 30, 'milanesa': 20}

# Consultar stock
producto = input("Ingrese el producto a consultar: ")
print(f"Stock de {producto}: {stock_productos.get(producto, 'No existe')}")

# Agrego unidades o nuevo producto
producto = input("Ingrese el producto para modificar/añadir: ")
unidades = int(input(f"Ingrese unidades para {producto}: "))
if producto in stock_productos:
    stock_productos[producto] += unidades
    print(f"Se agregaron {unidades} a {producto}. Nuevo stock: {stock_productos[producto]}")
else:
    stock_productos[producto] = unidades
    print(f"Producto {producto} añadido con stock: {unidades}")

# Mostrar inventario final
print("Inventario:", stock_productos)