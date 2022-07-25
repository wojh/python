#50 - Programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

sum = 0
for c in range(0, 6):
    num = int(input(f'Tecle o {c+1}° número inteiro: '))
    if num%2==0:
        sum += num

print(f"A soma de todos números pares inteiros inseridos é: {sum}")
