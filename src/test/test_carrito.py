from src.carrito import *
import unittest

class TestCarrito(unittest.TestCase):
    def setUp(self):
        self.carrito = Carrito()

    def test_agregar_producto(self):
        self.carrito.agregar_producto("Camiseta", 20.0)
        self.assertEqual(self.carrito.subtotal, 20.0)
        self.assertEqual(len(self.carrito.productos), 1)

        self.carrito.agregar_producto("Pantalón", 35.0)
        self.assertEqual(self.carrito.subtotal, 55.0)
        self.assertEqual(len(self.carrito.productos), 2)

    def test_calcular_total_sin_descuento(self):
        
        self.carrito.agregar_producto("Camiseta", 20.0)
        self.carrito.agregar_producto("Pantalón", 35.0)
        total = self.carrito.calcular_total()
        self.assertEqual(total, 55.0)  
    
    def test_calcular_total_con_descuento_0(self):
        
        self.carrito.agregar_producto("Camiseta", 20.0)
        self.carrito.agregar_producto("Pantalón", 35.0)
        total = self.carrito.calcular_total(0)
        self.assertEqual(total, 55.0)  

    def test_calcular_total_con_descuento_100(self):
        
        self.carrito.agregar_producto("Camiseta", 20.0)
        self.carrito.agregar_producto("Pantalón", 35.0)
        total = self.carrito.calcular_total(100)
        self.assertEqual(total, 0.0)  

    def test_calcular_total_con_descuento_10(self):
        
        self.carrito.agregar_producto("Camiseta", 20.0)
        self.carrito.agregar_producto("Pantalón", 35.0)
        total = self.carrito.calcular_total(10)
        self.assertEqual(total, 49.5)  

    def test_calcular_total_con_descuento_50(self):
        self.carrito.agregar_producto("Camiseta", 20.0)
        self.carrito.agregar_producto("Pantalón", 35.0)
        total = self.carrito.calcular_total(50)
        self.assertEqual(total, 27.5)  



if __name__ == "__main__":
    unittest.main()
