from src.gestionInventario import *
import unittest

class TestInventario(unittest.TestCase):
    def setUp(self):
        
        self.inventario = Inventario()

    def test_agregar_producto(self):
        
        self.inventario.agregar_producto(1, "Laptop", 10)
        self.assertIn(1, self.inventario.productos)
        self.assertEqual(self.inventario.productos[1].nombre, "Laptop")
        self.assertEqual(self.inventario.productos[1].cantidad, 10)

        
        self.inventario.agregar_producto(1, "Tablet", 5)
        self.assertEqual(self.inventario.productos[1].nombre, "Laptop")  
        self.assertEqual(self.inventario.productos[1].cantidad, 10)      

    def test_eliminar_producto(self):
        
        self.inventario.agregar_producto(1, "Laptop", 10)
        self.inventario.eliminar_producto(1)
        self.assertNotIn(1, self.inventario.productos)
        self.inventario.eliminar_producto(2)  

    def test_actualizar_stock(self):
        
        self.inventario.agregar_producto(1, "Laptop", 10)
        self.inventario.actualizar_stock(1, 5)
        self.assertEqual(self.inventario.productos[1].cantidad, 5)

        
        self.inventario.actualizar_stock(2, 20)  

    def test_consultar_producto(self):
        
        self.inventario.agregar_producto(1, "Laptop", 10)
        producto = self.inventario.consultar_producto(1)
        
        self.assertEqual(producto.id_producto, 1)
        self.assertEqual(producto.nombre, "Laptop")
        self.assertEqual(producto.cantidad, 10)


if __name__ == "__main__":
    unittest.main()
