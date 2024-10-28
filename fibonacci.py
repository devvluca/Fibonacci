def fibonacci_check(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number or number == 0

# Exemplo de uso:
number = int(input("Informe um número: "))
if fibonacci_check(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")
