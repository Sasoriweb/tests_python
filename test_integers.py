# hoy vamos a ver una manera distinta de hacer código.

# vamos a partir con Tests que fallen para hacerlos pasar :)


def test_integers_basic() -> None:
    # vamos a hacer primero una asignación de variable
    assert numero == 3

    # luego vamos a cambiar el valor de esta variable

    assert numero == 5

    # luego vamos a operar con otro integer con una suma

    assert suma == 10