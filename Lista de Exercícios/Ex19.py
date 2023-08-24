opc = input("Escolha a opção (Utilize A, B, C ou D): "
            "\nA - Soma de dois números"
            "\nB - Diferença de dois números (maior pelo menor)"
            "\nC - Produto entre dois números"
            "\nD - Divisão entre dois números (o denominador não pode ser zero)"
            "\n: ")

if opc == "A":
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    print(f"A soma dos dois números é: {num1 + num2}")

elif opc == "B":
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    print(f"A diferença dos dois números é: {max(num1, num2) - min(num1, num2)}")

elif opc == "C":
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    print(f"O produto dos dois números é: {num1 * num2}")

elif opc == "D":
    num1 = float(input("Número a ser divido: "))
    num2 = float(input("Denominador (Não pode ser 0): "))
    if num2 == 0:
        print("O denominador não pode ser 0!")
    else:
        print(f"A divisão dos dois números é: {num1 / num2}")

else:
    print("Opção Inválida!")