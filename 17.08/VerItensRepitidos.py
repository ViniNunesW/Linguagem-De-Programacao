A = ["Vinícius", "Gustavo", "Vinícius", "Gustavo"]
 
dup = {x for x in A if A.count(x) > 1}
print(dup)