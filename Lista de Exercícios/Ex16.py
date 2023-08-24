esc = input("Digite (C ou F)"
            "\nC - Passar de °C para °F"
            "\nF - Passar de °F para °C"
            "\n:")

if esc == "C":
    temp = float(input("Temperatura em °C: "))
    print(f"Temperatura em graus F°: {(temp * 1.8) + 32}")
elif esc == "F":
    temp = float(input("Temperatura em °F: "))
    print(f"Temperatura em °C: {(temp - 32) / 1.8}")
else:
    print("Escolha inválida!")