# hoy vamos a ver una manera distinta de hacer código.

# vamos a partir con Tests que fallen para hacerlos pasar :)


def test_strings_basic() -> None:

    string = "perrito" # vamos a hacer primero una asignación de variable
    assert string == "perrito"

    # luego vamos a cambiar el valor de esta variable
    string = "gatito"
    assert string == "gatito"

    # luego vamos a transformar ese string a otro casing
    upper_string = string.upper()
    assert upper_string == "GATITO"

    # ahora intentemos obtener los primeros tres caracteres del string
    substring = upper_string[0:3]
    assert substring == "GAT"

def test_strings_concat() -> None:
    # partimos con un string y lo vamos a concatenar
    perrito = "perrito" 
    assert perrito == "perrito"
    frase = "Un "+ perrito + " tiene hambre"
    assert frase == "Un perrito tiene hambre"

def test_string_integers() -> None:
    integer = 20 # definimos un integer
    assert integer == 20

    # lo convertimos a string
    str_integer = str(integer)
    assert str_integer == "20"

    # lo podemos operar con otros strings@
    frase = "Yo tenía " + str_integer + " perritos"
    assert frase == "Yo tenía 20 perritos"

