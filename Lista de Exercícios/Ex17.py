altura = float(input("Altura: "))
sexo = input("Sexo (Utilize M ou F): "
             "\nM - Masculino"
             "\nF - Feminino"
             "\n: ")

if sexo == "M":
    print(f"Peso ideal: {(72.7 * altura) - 58}")
elif sexo == "F":
    print(f"Peso ideal: {(62.1 * altura) - 44.7}")
else:
    print("Resposta Inválida")