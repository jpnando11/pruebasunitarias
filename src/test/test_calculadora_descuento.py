from src.calculadoraDescuento import *
import unittest

class TestCalculadoraDescuento(unittest.TestCase):

    def test_calcular_precio_final_con_descuento(self):
        calculadora = CalculadoraDescuento(precio_original=200, porcentaje_descuento=20)
        self.assertEqual(calculadora.calcular_precio_final(), 160)

    def test_calcular_precio_final_sin_descuento(self):
        calculadora = CalculadoraDescuento(precio_original=100, porcentaje_descuento=0)
        self.assertEqual(calculadora.calcular_precio_final(), 100)

    def test_calcular_precio_final_con_descuento_completo(self):
        calculadora = CalculadoraDescuento(precio_original=150, porcentaje_descuento=100)
        self.assertEqual(calculadora.calcular_precio_final(), 0)

    def test_precio_invalido(self):
        with self.assertRaises(ValueError) as context:
            calculadora = CalculadoraDescuento(precio_original=0, porcentaje_descuento=10)
            calculadora.calcular_precio_final()
        self.assertEqual(str(context.exception), "El precio original debe ser mayor que cero.")

        with self.assertRaises(ValueError) as context:
            calculadora = CalculadoraDescuento(precio_original=-50, porcentaje_descuento=10)
            calculadora.calcular_precio_final()
        self.assertEqual(str(context.exception), "El precio original debe ser mayor que cero.")

    def test_descuento_invalido(self):
        with self.assertRaises(ValueError) as context:
            calculadora = CalculadoraDescuento(precio_original=100, porcentaje_descuento=110)
            calculadora.calcular_precio_final()
        self.assertEqual(str(context.exception), "El porcentaje de descuento debe estar entre 0 y 100.")

        with self.assertRaises(ValueError) as context:
            calculadora = CalculadoraDescuento(precio_original=100, porcentaje_descuento=-10)
            calculadora.calcular_precio_final()
        self.assertEqual(str(context.exception), "El porcentaje de descuento debe estar entre 0 y 100.")
    
if __name__ == "__main__":
    unittest.main()
