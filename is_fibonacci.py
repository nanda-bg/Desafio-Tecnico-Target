def is_fibonacci(number):
    a, b = 0, 1

    while a < number:
        a, b = b, a + b

    message = f"{number} está na sequência de Fibonacci" if a == number else f"{number} não está na sequência de Fibonacci"
    
    return message


def teste():
    print(is_fibonacci(0))  # esperado: True
    print(is_fibonacci(1))  # esperado: True
    print(is_fibonacci(2))  # esperado: True
    print(is_fibonacci(3))  # esperado: True
    print(is_fibonacci(4))  # esperado: False
    print(is_fibonacci(5))  # esperado: True
    print(is_fibonacci(6))  # esperado: False
    print(is_fibonacci(8))  # esperado: True
    print(is_fibonacci(13)) # esperado: True
    print(is_fibonacci(21)) # esperado: True
    print(is_fibonacci(22)) # esperado: False
    print(is_fibonacci(34)) # esperado: True
    print(is_fibonacci(35)) # esperado: False
    print(is_fibonacci(144))# esperado: True
    print(is_fibonacci(145))# esperado: False




number = int(input("Informe o valor para verificação: "))
print(is_fibonacci(number))