# ERR5x3 -4.5
# para realizar el test se debe descargar pytest en la carpeta contenedora
# y despues dirigirse en la consola de comandos a la direccion de la carpeta
# posteriormente se escribe en la consola "pytest Tarea1_Prueba.py"


import pytest
from Tarea1 import check_char, caps_switch  # tilizar funciones otros programas


@pytest.mark.parametrize(  # permite proponer parametros en tuplas
    "charr,resp",  # Cada letra debe retornar 0
    [
        ("A", 0), ("a", 0),
        ("B", 0), ("b", 0),
        ("C", 0), ("c", 0),
        ("D", 0), ("d", 0),
        ("E", 0), ("e", 0),
        ("F", 0), ("f", 0),
        ("G", 0), ("g", 0),
        ("H", 0), ("h", 0),
        ("I", 0), ("i", 0),
        ("J", 0), ("j", 0),
        ("K", 0), ("k", 0),
        ("L", 0), ("l", 0),
        ("M", 0), ("m", 0),
        ("N", 0), ("n", 0),
        ("O", 0), ("o", 0),
        ("P", 0), ("p", 0),
        ("Q", 0), ("q", 0),
        ("R", 0), ("r", 0),
        ("S", 0), ("s", 0),
        ("T", 0), ("t", 0),
        ("U", 0), ("u", 0),
        ("V", 0), ("v", 0),
        ("W", 0), ("w", 0),
        ("X", 0), ("x", 0),
        ("Y", 0), ("y", 0),
        ("Z", 0), ("z", 0)
    ])
def test_check_char(charr, resp):
    assert check_char(charr) == resp  # comprobar las tuplas


@pytest.mark.parametrize(
    "charr2,resp2",  # cada letra retorna mayuscula
    [
        ("A", "a"), ("a", "A"),
        ("B", "b"), ("b", "B"),
        ("C", "c"), ("c", "C"),
        ("D", "d"), ("d", "D"),
        ("E", "e"), ("e", "E"),
        ("F", "f"), ("f", "F"),
        ("G", "g"), ("g", "G"),
        ("H", "h"), ("h", "H"),
        ("I", "i"), ("i", "I"),
        ("J", "j"), ("j", "J"),
        ("K", "k"), ("k", "K"),
        ("L", "l"), ("l", "L"),
        ("M", "m"), ("m", "M"),
        ("N", "n"), ("n", "N"),
        ("O", "o"), ("o", "O"),
        ("P", "p"), ("p", "P"),
        ("Q", "q"), ("q", "Q"),
        ("R", "r"), ("r", "R"),
        ("S", "s"), ("s", "S"),
        ("T", "t"), ("t", "T"),
        ("U", "u"), ("u", "U"),
        ("V", "v"), ("v", "V"),
        ("W", "w"), ("w", "W"),
        ("X", "x"), ("x", "X"),
        ("Y", "y"), ("y", "Y"),
        ("Z", "z"), ("z", "Z")
    ])
def test_caps_switch(charr2, resp2):
    assert caps_switch(charr2) == resp2  # comprobar tuplas


# Comprobar errores
def test_error_b():
    assert check_char("AZ") == 0


def test_error_c():
    assert check_char("1") == 0


def test_error_d():
    assert check_char(12) == 0
