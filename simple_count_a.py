def remove_acento_a(frase):
    tabela_de_acento = str.maketrans(
        'àáâãä',
        'aaaaa'
    )
    return frase.translate(tabela_de_acento)


def simple_count_a(frase):
    return remove_acento_a(frase.lower()).count("a")


def teste():
    print(simple_count_a("Abril"))            # esperado: 1
    print(simple_count_a("Banana"))           # esperado: 3
    print(simple_count_a("Casa"))             # esperado: 2
    print(simple_count_a("Python"))           # esperado: 0
    print(simple_count_a("Aprendizado"))      # esperado: 2
    print(simple_count_a("Automóvel"))        # esperado: 1
    print(simple_count_a("Algoritmo"))        # esperado: 1
    print(simple_count_a("Programação"))      # esperado: 3
    print(simple_count_a("Misteriosa"))       # esperado: 1
    print(simple_count_a("Matemática"))       # esperado: 3



frase = input("Informe a frase para verificação: ")
print(simple_count_a(frase))