def reverse(frase):
    tamanho = len(frase)

    frase_reverse = ""
    for i in range(1, tamanho + 1, 1):
        frase_reverse += frase[-i]

    return frase_reverse

def teste():
    resultado = reverse("Hello, world! This is a test.")
    esperado = ".tset a si sihT !dlrow ,olleH"
    assert resultado == esperado, f"Erro: Esperado '{esperado}', mas obteve '{resultado}'"
    
  
    resultado = reverse("Python programming is fun!")
    esperado = "!nuf si gnimmargorp nohtyP"
    assert resultado == esperado, f"Erro: Esperado '{esperado}', mas obteve '{resultado}'"
    

    resultado = reverse("Data Science is the future.")
    esperado = ".erutuf eht si ecneicS ataD"
    assert resultado == esperado, f"Erro: Esperado '{esperado}', mas obteve '{resultado}'"
    
    print("Todos os testes passaram com sucesso!")


frase = input("Informe a frase para verificação: ")
print(reverse(frase))