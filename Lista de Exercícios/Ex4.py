algo = input("Digite alguma coisa: ")

print(f"{type(algo)}\nNumero: {algo.isnumeric()}\nLetra: {algo.isalpha()}\nAlfanumérico: {algo.isalnum()}"
f"\nMinusculo: {algo.islower()}\nMaiusculo: {algo.isupper()}\nEspaço Vazio: {algo.isspace()}\nTitulo {algo.istitle()}")