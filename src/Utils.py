from datetime import datetime
import string
import random

class Utils:

    def es_par(num):
        is_par = False
        if num % 2 == 0:
            is_par = True
        return is_par

    def calcular_edad(fecha_nacimiento):
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        fecha_actual = datetime.now()
        if fecha_nacimiento > fecha_actual:
            return "Fecha invalida"
        edad = fecha_actual.year - fecha_nacimiento.year
        return edad

    def generar_id():
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choices(caracteres, k=8))

    def  ordenar_por_longitud(lista_palabras):
        return sorted(lista_palabras, key=len)
