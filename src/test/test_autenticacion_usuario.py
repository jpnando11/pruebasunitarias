from src.AutenticacionUsuario import *
import unittest

class TestSistemaAutenticacion(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaAutenticacion()

    def test_registrar_usuario_exitoso(self):
        self.sistema.registrar_usuario("usuario1", "contraseña123", "usuario1@example.com")
        self.assertIn("usuario1", self.sistema.usuarios)
        self.assertEqual(self.sistema.usuarios["usuario1"].correo, "usuario1@example.com")

    def test_iniciar_sesion_exitoso(self):
        self.sistema.registrar_usuario("usuario1", "contraseña123", "usuario1@example.com")
        self.assertTrue(self.sistema.iniciar_sesion("usuario1", "contraseña123"))
        self.assertTrue(self.sistema.usuarios["usuario1"].sesion_activa)


    def test_cerrar_sesion_exitoso(self):
        self.sistema.registrar_usuario("usuario1", "contraseña123", "usuario1@example.com")
        self.sistema.iniciar_sesion("usuario1", "contraseña123")
        self.sistema.cerrar_sesion("usuario1")
        self.assertFalse(self.sistema.usuarios["usuario1"].sesion_activa)


    def test_recuperar_contraseña_usuario_existente(self):
        self.sistema.registrar_usuario("usuario1", "contraseña123", "usuario1@example.com")
        a = self.sistema.recuperar_contraseña("usuario1")   
        assert "Enlace de recuperación de contraseña enviado a usuario1@example.com." == a

if __name__ == "__main__":
    unittest.main()
