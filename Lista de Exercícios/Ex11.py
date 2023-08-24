nome = input("Nome: ")
horas = float(input("Horas trabalhadas: "))
valor = float(input("Valor da hora trabalhada: "))

salB = horas * valor

print(f"------Folha de Pagamento ({nome})------")
print(f"Salário final (Desconto INSS): {salB - (salB * 0.05)}")
