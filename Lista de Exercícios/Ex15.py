temp = float(input("Temperatura atual (° celsius): "))

if temp < 20:
    print(f"A temperatura de {temp}° está fria.")
elif (temp >= 20) and (temp <= 25):
    print(f"A temperatura de {temp}° está agradável.")
else:
    print(f"A temperatura de {temp}° está quente.")