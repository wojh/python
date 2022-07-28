# 66 - Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

s = count = int(0)

while True:
    print("Para parar, insira 999")
    n = int(input("Insira um número inteiro: "))
    if n == 999:
        break
    s += n
    count += 1 
    print('')

print('')
print(f"Você digitou {count} números, e a soma entre eles é {s}")
