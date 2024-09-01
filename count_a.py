def remove_acento_a(frase):
    tabela_de_acento = str.maketrans(
        'àáâãä',
        'aaaaa'
    )
    return frase.translate(tabela_de_acento)


def count_a(frase):
    frase = remove_acento_a(frase.lower())

    qnts_a = 0

    for letra in frase:
        if letra == "a":
            qnts_a += 1

    return qnts_a


def teste():
    print(count_a("Abril"))            # esperado: 1
    print(count_a("Banana"))           # esperado: 3
    print(count_a("Casa"))             # esperado: 2
    print(count_a("Python"))           # esperado: 0
    print(count_a("Aprendizado"))      # esperado: 2
    print(count_a("Automóvel"))        # esperado: 1
    print(count_a("Algoritmo"))        # esperado: 1
    print(count_a("Programação"))      # esperado: 3
    print(count_a("Misteriosa"))       # esperado: 1
    print(count_a("Matemática"))       # esperado: 3



frase = input("Informe a frase para verificação: ")
print(count_a(frase))