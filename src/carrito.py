class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []  # Lista para almacenar productos
        self.subtotal = 0.0  # Subtotal inicial

    def agregar_producto(self, nombre, precio):
        producto = Producto(nombre, precio)
        self.productos.append(producto)
        self.subtotal += precio
        print(f"Producto '{nombre}' agregado con precio {precio:.2f}. Subtotal actual: {self.subtotal:.2f}")

    def calcular_total(self, descuento=0):
        if descuento < 0 or descuento > 100:
            print("Error: El descuento debe estar entre 0 y 100.")
            return None
        descuento_aplicado = self.subtotal * (descuento / 100)
        total = self.subtotal - descuento_aplicado
        print(f"Subtotal: {self.subtotal:.2f}")
        print(f"Descuento aplicado: {descuento}% ({descuento_aplicado:.2f})")
        print(f"Total final: {total:.2f}")
        return total
