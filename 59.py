#59 - Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar 
#[2] multiplicar 
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

option = 0

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))

print('')
print("Abaixo segue seu menu!!!")

sleep(1)
print('')

print("""[1] somar
[2] multiplicar
[3] maior número
[4] novos números
[5] sair do programa""")

sleep(0.5)
print('')

option = int(input("Qual sua opção [1, 2, 3, 4 ou 5]: "))

if option == 5:
    print("Fim do Programa!!!")

while option != 5:
    if option == 1:
        print(f"A soma é: {num1+num2}")
    elif option == 2:
        print(f"A multiplicação é: {num*num2}")
    elif option == 3:
        if num2 < num1:
            print(f"O maior número é: {num1}")
        elif num2>num1:
            print(f"O maior número é: {num2}")
        else:
            print('Ambos são iguais!!!')
    elif option == 4:
        print(f"A soma é: {num1+num2}")
    elif option == 5:
        print(f"A soma é: {num1+num2}")
    else:
        print("Opção INVÁLIDA!!!")
