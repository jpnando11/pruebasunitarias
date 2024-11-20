from datetime import datetime

class Reserva:
    def __init__(self, usuario, fecha, hora, numero_personas):
        self.usuario = usuario
        self.fecha = fecha
        self.hora = hora
        self.numero_personas = numero_personas

    def __str__(self):
        return f"Reserva para {self.numero_personas} personas el {self.fecha} a las {self.hora}."

class SistemaReservas:
    def __init__(self, capacidad_por_hora):
        # Capacidad máxima de personas por hora
        self.capacidad_por_hora = capacidad_por_hora
        # Diccionario para almacenar reservas, con (fecha, hora) como clave
        self.reservas = {}

    def crear_reserva(self, usuario, fecha, hora, numero_personas):
        clave = (fecha, hora)

        # Verificar si hay disponibilidad
        if not self.verificar_disponibilidad(fecha, hora, numero_personas):
            raise ValueError("No hay disponibilidad para la fecha y hora especificada.")
        
        # Crear la lista de reservas para esa fecha y hora si no existe
        if clave not in self.reservas:
            self.reservas[clave] = []
        
        # Crear la reserva y añadirla al sistema
        nueva_reserva = Reserva(usuario, fecha, hora, numero_personas)
        self.reservas[clave].append(nueva_reserva)
        print(f"Reserva creada para {usuario}: {nueva_reserva}")

    def cancelar_reserva(self, usuario, fecha, hora):
        clave = (fecha, hora)

        # Verificar si hay reservas en la fecha y hora especificada
        if clave in self.reservas:
            # Buscar la reserva del usuario y eliminarla
            for reserva in self.reservas[clave]:
                if reserva.usuario == usuario:
                    self.reservas[clave].remove(reserva)
                    print(f"Reserva cancelada para {usuario}.")
                    return
            print("No se encontró una reserva para el usuario en la fecha y hora especificada.")
        else:
            print("No hay reservas en la fecha y hora especificada.")

    def verificar_disponibilidad(self, fecha, hora, numero_personas):
        clave = (fecha, hora)
        
        # Verificar la capacidad restante en la fecha y hora especificada
        personas_reservadas = sum(reserva.numero_personas for reserva in self.reservas.get(clave, []))
        return (personas_reservadas + numero_personas) <= self.capacidad_por_hora

    def listar_reservas_usuario(self, usuario):
        # Filtrar y mostrar todas las reservas para el usuario
        reservas_usuario = [
            reserva for reservas in self.reservas.values()
            for reserva in reservas if reserva.usuario == usuario
        ]
        
        if reservas_usuario:
            print(f"Reservas para {usuario}:")
            for reserva in reservas_usuario:
                print(reserva)
        else:
            print(f"No hay reservas para el usuario {usuario}.")
