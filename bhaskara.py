def main():
    print("Bem-vindo ao Calcula Bhaskara!")
    while True:
        try:
            a = float(input("Digite o coeficiente a: "))
            break
        except:
            print("Valor inválido.")

    while True:
        try:
            b = float(input("Digite o coeficiente b: "))
            break
        except:
            print("Valor inválido.")

    while True:
        try:
            c = float(input("Digite o coeficiente c: "))
            break
        except:
            print("Valor inválido.")

    delta = calcula_delta(a, b, c)
    if delta < 0:
        print("Essa equação não possui raízes reais.")
    else:
        raizes = resultado(a, b, delta)
        trata_resultado(raizes)


def calcula_delta(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    return delta


def resultado(a, b, delta):
    resultado1 = (((-1) * b) + delta ** (1 / 2)) / (2 * a)
    resultado2 = (((-1) * b) - delta ** (1 / 2)) / (2 * a)
    return [resultado1, resultado2]


def trata_resultado(resultados):
    if resultados[0] == resultados[1]:
        print("A raiz da equação é:", resultados[0])
    else:
        print("As raízes da equação são:", resultados[0], "e", resultados[1])


main()
