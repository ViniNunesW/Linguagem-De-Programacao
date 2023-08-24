a = ["Rodolfo", "Gustavo", "Luan", "Clash", "Fernando", "Ex-Líder", "Nunes"] #Lista
print(a)
print(a[0])

#Inserir item na lista
a.append("Royale")
print(a)

a.insert(1, "Kurireba") #Inserir um item na lista em uma posição específica
print(a)

a[0] = "Kuririn" #Substituir item da lista
print(a)

print(a[:3]) #Antes do index 3
print(a[3:]) #Depois do index 3
print(a[1:4]) #Entre o 1 e o 3 index

del a[0] #Remover item pelo index
a.remove("Clash") #Remover item pelo nome
b = a.pop(0) #Transfere um item para outra variável
print(a)
print(b)

a.clear() #Limpa toda a lista

c = a.copy() #Copia a lista para outra variável
print(a)
print(c)

d = a + c #Juntar listas

a.append("Nunes")

print(d)

print(a.count("Nunes")) #Conta quantos itens iguais tem no parâmetro passado

print(len(a)) #Conta o total de itens da lista

print(a.index("Nunes")) #Verfica em qual posição se encontra na lista

val = [1, 2, 3, 4, 5]

val.sort()
print(sorted(val))
val.reverse()

min = min(val) #Valor mínimo 
max = max(val) #Valor máximo
soma = sum(val) #Soma dos valores

print(f"O valor mínimo é {min}, o valor máximo é {max} e a soma de todos os números é {soma}.")

if "Nunes" in a :
    print("Nunes está na lista")
else:
    print("Nunes não está na lista")