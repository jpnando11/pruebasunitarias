from src.Utils import *
import unittest

def test_es_par():
    test1 = Utils.es_par(4)
    test2 = Utils.es_par(7)
    test3 = Utils.es_par(0)
    test4 = Utils.es_par(-2)
    assert test1 == True
    assert test2 == False
    assert test3 == True
    assert test4 == True

def test_calcular_edad():
    test1 = Utils.calcular_edad("2000-01-01")
    test2 = Utils.calcular_edad("2024-01-01")
    test3 = Utils.calcular_edad("1990-09-28")
    
    
    assert test1 == 24
    assert test2 == 0
    assert test3 == 34

def test_calcular_edad_con_fecha_futura():
    test4 = Utils.calcular_edad("2030-01-01")
    assert test4 == "Fecha invalida"


def test_generar_id():
    test1 = Utils.generar_id()
    assert len(test1) == 8


def test_ordenar_por_longitud():
    palabras1 = ["perro", "gato", "elefante"]
    palabras2 = ["sol", "estrella", "luna"]
    palabras3 = ["sol", "sol", "sol"]
    
    resultado1 = Utils.ordenar_por_longitud(palabras1)
    resultado2 = Utils.ordenar_por_longitud(palabras2)
    resultado3 = Utils.ordenar_por_longitud([])
    resultado4 = Utils.ordenar_por_longitud(palabras3)
    
    assert resultado1 == ["gato", "perro", "elefante"]
    assert resultado2 == ["sol", "luna", "estrella"]
    assert resultado3 == []
    assert resultado4 == ["sol", "sol", "sol"]