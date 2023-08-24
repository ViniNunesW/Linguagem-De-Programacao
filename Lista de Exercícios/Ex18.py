nota1 = float(input("Nota 1 (Peso 5): "))

if (nota1 >= 0) and (nota1 <= 5):
    nota2 = float(input("Nota 2: (Peso 5): "))
    if (nota2 >= 0) and (nota2 <= 5):
        nota3 = float(input("Nota 3: (Peso 10): "))
        if (nota3 >= 0) and (nota3 <= 10):
            print(f"A média das três notas é: {((nota1 + nota2) + nota3) / 2}")
        else:
            print("A nota 3 deve ser entre 0 e 10!")
    else:
        print("A nota 2 deve ser entre 0 e 5!")
else:
    print("A nota 2 deve ser entre 0 e 5!")