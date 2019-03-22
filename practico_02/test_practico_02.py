from . import ejercicio_01 as ej01
from . import ejercicio_02 as ej02
from . import ejercicio_03 as ej03
from . import ejercicio_04 as ej04
from . import ejercicio_05 as ej05
from . import ejercicio_06 as ej06

import math

def test_rectangulo():
    rect = ej01.Rectangulo(5, 5)
    assert rect.area() == 25

def test_circulo():
    circ = ej02.Circulo(1)
    assert circ.area() == math.pi

def test_persona():
    per = ej03.Persona("Ezequiel", 23, "M", 85, 168)
    assert per.dni == "00000001"

    per = ej03.Persona("Francisco", 40, "M", 70, 158)
    assert per.dni == "00000002"

def test_estudiante():
    est = ej04.Estudiante("Ezequiel", 23, "M", 85, 168, "ISI", 2015, 28, 41)
    assert est.edad_ingreso() == 19
    assert est.avance() == "68.29%"

def test_carreras():
    est = ej04.Estudiante("Ezequiel", 23, "M", 85, 168, "ISI", 2015, 28, 41)
    est2 = ej04.Estudiante("Ezequiel", 18, "M", 80, 175, "IM", 2018, 3, 41)
    est3 = ej04.Estudiante("Ezequiel", 24, "M", 90, 190, "IQ", 2014, 30, 41)
    est4 = ej04.Estudiante("Ezequiel", 26, "M", 70, 145, "ISI", 2012, 34, 41)
    list_est = [est, est2, est3, est4]

    assert ej05.organizar_estudiantes(list_est) == {'IM': 1, 'IQ': 1, 'ISI': 2}
    
def test_edad():
    per = ej06.Persona('1995.12.14')
    assert per.edad() == 23
