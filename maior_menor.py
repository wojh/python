#55 - Programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for c in range(1, 2):
    peso = float(input(f"Peso da pessoa {c}: "))
    maior = float(peso)
    menor = float(peso)
    
for c in range(2,6):
    peso = float(input(f"Peso da pessoa {c}: "))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    
print(f"Maior: {maior} e menor: {menor}")
