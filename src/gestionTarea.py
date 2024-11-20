from datetime import datetime

class Tarea:
    def __init__(self, titulo, fecha_vencimiento):
        self.titulo = titulo
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.titulo} - Vence el {self.fecha_vencimiento} - Estado: {estado}"

class SistemaTareas:
    def __init__(self):
        self.tareas = []

    def crear_tarea(self, titulo, fecha_vencimiento):
        nueva_tarea = Tarea(titulo, fecha_vencimiento)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{titulo}' creada con éxito.")

    def marcar_tarea_completada(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo and not tarea.completada:
                tarea.completada = True
                print(f"Tarea '{titulo}' marcada como completada.")
                return
        print(f"No se encontró una tarea pendiente con el título '{titulo}'.")

    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print(f"Tarea '{titulo}' eliminada.")
                return
        print(f"No se encontró una tarea con el título '{titulo}'.")

    def listar_tareas_pendientes(self):
        tareas_pendientes = [tarea for tarea in self.tareas if not tarea.completada]
        if tareas_pendientes:
            print("Tareas pendientes:")
            for tarea in tareas_pendientes:
                print(tarea)
        else:
            print("No hay tareas pendientes.")