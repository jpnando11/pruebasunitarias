import hashlib

class Usuario:
    def __init__(self, nombre_usuario, contraseña, correo):
        self.nombre_usuario = nombre_usuario
        # Guardamos la contraseña encriptada para mayor seguridad
        self.contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
        self.correo = correo
        self.sesion_activa = False  # Estado de la sesión

class SistemaAutenticacion:
    def __init__(self):
        # Diccionario para almacenar usuarios, con el nombre de usuario como clave
        self.usuarios = {}

    def registrar_usuario(self, nombre_usuario, contraseña, correo):
        if nombre_usuario in self.usuarios:
            raise ValueError("El nombre de usuario ya está en uso.")
        if "@" not in correo:
            raise ValueError("El correo no es válido.")
        
        self.usuarios[nombre_usuario] = Usuario(nombre_usuario, contraseña, correo)
        print(f"Usuario '{nombre_usuario}' registrado con éxito.")

    def iniciar_sesion(self, nombre_usuario, contraseña):
        if nombre_usuario not in self.usuarios:
            raise ValueError("El usuario no existe.")
        
        usuario = self.usuarios[nombre_usuario]
        contraseña_encriptada = hashlib.sha256(contraseña.encode()).hexdigest()
        
        if usuario.contraseña == contraseña_encriptada:
            usuario.sesion_activa = True
            print(f"Usuario '{nombre_usuario}' ha iniciado sesión con éxito.")
            return True
        else:
            raise ValueError("Contraseña incorrecta.")

    def cerrar_sesion(self, nombre_usuario):
        if nombre_usuario not in self.usuarios:
            raise ValueError("El usuario no existe.")
        
        usuario = self.usuarios[nombre_usuario]
        
        if usuario.sesion_activa:
            usuario.sesion_activa = False
            print(f"Usuario '{nombre_usuario}' ha cerrado sesión.")
        else:
            print(f"El usuario '{nombre_usuario}' no tiene una sesión activa.")

    def recuperar_contraseña(self, nombre_usuario):
        if nombre_usuario not in self.usuarios:
            raise ValueError("El usuario no existe.")
        usuario = self.usuarios[nombre_usuario]
        return f"Enlace de recuperación de contraseña enviado a {usuario.correo}."
