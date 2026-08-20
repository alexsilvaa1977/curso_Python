"""Módulo de exemplo usado pelo notebook desta aula."""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


if __name__ == "__main__":
    print("Testando o módulo diretamente:")
    print("somar(2, 3) =", somar(2, 3))
    print("subtrair(5, 2) =", subtrair(5, 2))
