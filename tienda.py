from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, nombre, precio, stock=0):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                producto.set_stock(producto.get_stock() + stock)
                return
        self.__productos.append(Producto(nombre, precio, stock))

    def listar_productos(self):
        products_info = []
        for producto in self._Tienda__productos:
            products_info.append(f"{producto.get_nombre()}: ${producto.get_precio()}")
        return '\n'.join(products_info)

    def realizar_venta(self, nombre_producto, cantidad):
        pass  # Este método se implementará en las clases hijas

class Restaurante(Tienda):
    def realizar_venta(self, nombre_producto, cantidad):
        print(f"Se ha vendido {cantidad} unidades de {nombre_producto}")

class Supermercado(Tienda):
    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self._Tienda__productos:
            if producto.get_nombre() == nombre_producto:
                if cantidad <= producto.get_stock():
                    producto.set_stock(producto.get_stock() - cantidad)
                    print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                else:
                    print("No hay suficiente stock disponible")

    def listar_productos(self):
        products_info = []
        for producto in self._Tienda__productos:
            stock_info = f"Pocos productos disponibles - Stock: {producto.get_stock()}" if producto.get_stock() < 10 else f"Stock: {producto.get_stock()}"
            products_info.append(f"{producto.get_nombre()}: ${producto.get_precio()} - {stock_info}")
        return '\n'.join(products_info)

class Farmacia(Tienda):
    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self._Tienda__productos:
            if producto.get_nombre() == nombre_producto:
                if cantidad <= producto.get_stock() and cantidad <= 3:
                    producto.set_stock(producto.get_stock() - cantidad)
                    print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                elif cantidad > 3:
                    print("No se puede vender más de 3 unidades por venta")
                else:
                    print("No hay suficiente stock disponible")

    def listar_productos(self):
        products_info = []
        for producto in self._Tienda__productos:
            delivery_info = "Envío gratis al solicitar este producto" if producto.get_precio() > 15000 else ""
            products_info.append(f"{producto.get_nombre()}: ${producto.get_precio()} {delivery_info}")
        return '\n'.join(products_info)