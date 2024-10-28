def count_a(string):
    count = string.lower().count('a')
    if count > 0:
        print(f"A letra 'a' aparece {count} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Exemplo de uso:
string = input("Digite uma string: ")
count_a(string)
