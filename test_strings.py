# hoy vamos a ver una manera distinta de hacer código.

# vamos a partir con Tests que fallen para hacerlos pasar :)


def test_strings_basic() -> None:
    # vamos a hacer primero una asignación de variable
    assert string == "perrito"

    # luego vamos a cambiar el valor de esta variable

    assert string == "gatito"

    # luego vamos a transformar ese string a otro casing

    assert upper_string == "GATITO"

    # ahora intentemos obtener los primeros tres caracteres del string

    assert substring == "GAT"

def test_strings_concat() -> None:
    # partimos con un string y lo vamos a concatenar

    assert perrito == "perrito"

    assert frase == "Un perrito tiene hambre"

def test_string_integers() -> None:
    # definimos un integer
    assert integer == 20

    # lo convertimos a string

    assert str_integer == "20"

    # lo podemos operar con otros strings@

    assert frase == "Yo tenía 20 perritos"

