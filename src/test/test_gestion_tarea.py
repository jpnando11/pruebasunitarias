import unittest
from datetime import datetime, timedelta
from src.gestionTarea import *

class TestSistemaTareas(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaTareas()
        self.fecha_vencimiento = datetime.now() + timedelta(days=5)

    def test_crear_tarea(self):
        self.sistema.crear_tarea("Estudiar para el examen", self.fecha_vencimiento)
        self.assertEqual(len(self.sistema.tareas), 1)
        self.assertEqual(self.sistema.tareas[0].titulo, "Estudiar para el examen")
        self.assertEqual(self.sistema.tareas[0].fecha_vencimiento, self.fecha_vencimiento)
        self.assertFalse(self.sistema.tareas[0].completada)

    def test_marcar_tarea_completada_existente(self):
        self.sistema.crear_tarea("Hacer ejercicio", self.fecha_vencimiento)
        self.sistema.marcar_tarea_completada("Hacer ejercicio")
        self.assertTrue(self.sistema.tareas[0].completada)

    def test_marcar_tarea_completada_inexistente(self):
        with self.assertLogs() as log:
            self.sistema.marcar_tarea_completada("Tarea no existente")
            self.assertIn("No se encontró una tarea pendiente con el título 'Tarea no existente'.", log.output[-1])

    def test_eliminar_tarea_existente(self):
        self.sistema.crear_tarea("Leer libro", self.fecha_vencimiento)
        self.sistema.eliminar_tarea("Leer libro")
        self.assertEqual(len(self.sistema.tareas), 0)

    def test_eliminar_tarea_inexistente(self):
        with self.assertLogs() as log:
            self.sistema.eliminar_tarea("Tarea no existente")
            self.assertIn("No se encontró una tarea con el título 'Tarea no existente'.", log.output[-1])

    def test_listar_tareas_pendientes_con_tareas(self):
        self.sistema.crear_tarea("Comprar víveres", self.fecha_vencimiento)
        self.sistema.crear_tarea("Lavar el auto", self.fecha_vencimiento)
        with self.assertLogs() as log:
            self.sistema.listar_tareas_pendientes()
            self.assertIn("Tareas pendientes:", log.output[0])
            self.assertIn("Comprar víveres", log.output[1])
            self.assertIn("Lavar el auto", log.output[2])

    def test_listar_tareas_pendientes_sin_tareas(self):
        with self.assertLogs() as log:
            self.sistema.listar_tareas_pendientes()
            self.assertIn("No hay tareas pendientes.", log.output[-1])
if __name__ == "__main__":
    unittest.main()
