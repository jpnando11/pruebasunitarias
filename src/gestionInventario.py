class Producto:
    def __init__(self, id_producto, nombre, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad

class Inventario:
    def __init__(self):
        self.productos = {}  # Usamos un diccionario para almacenar los productos por su ID

    def agregar_producto(self, id_producto, nombre, cantidad):
        if id_producto in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            nuevo_producto = Producto(id_producto, nombre, cantidad)
            self.productos[id_producto] = nuevo_producto
            print(f"Producto '{nombre}' agregado al inventario.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado del inventario.")
        else:
            print("Error: El producto no existe en el inventario.")

    def actualizar_stock(self, id_producto, nueva_cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].cantidad = nueva_cantidad
            print(f"Stock del producto con ID {id_producto} actualizado a {nueva_cantidad}.")
        else:
            print("Error: El producto no existe en el inventario.")

    def consultar_producto(self, id_producto):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}")
            return producto
        else:
            print("Error: El producto no existe en el inventario.")
            return None

