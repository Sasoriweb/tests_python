# hoy vamos a ver una manera distinta de hacer código.

# vamos a partir con Tests que fallen para hacerlos pasar :)


def test_integers_basic() -> None:
    
    numero = 3 # vamos a hacer primero una asignación de variable
    assert numero == 3

    # luego vamos a cambiar el valor de esta variable
    numero = 5
    assert numero == 5

    # luego vamos a operar con otro integer con una suma
    suma = numero + 5
    assert suma == 10

    # ahora intentemos hacer una división
    division = suma / numero
    assert division == 2

def test_integers_string() -> None:
    # partimos con un integer y transformemoslo a string
    str_numero = "3"
    assert str_numero == "3"

    # luego veamos si podemos transformar ese str a int
    numero = int(str_numero)
    assert numero == 3