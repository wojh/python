# 68 - Faça um program que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador PERDER, mostrando 
# o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

count = win = int(0)

while True:
    n_user = int(input("Qual número escolhe ?? "))
    p_i = input("Par ou Ímpar [p/i]: ").lower()
    
    while (p_i != 'p' and p_i != 'i'):
        p_i = input("Par ou Ímpar [p/i]: ").lower()
    
    count += 1
    n_comp = int(randint(0, 2))
    
    print('')
    print(f"Computador escolheu {n_comp}")
    total = n_comp + n_user
    print('')
    
    if total % 2 == 0:
        print("Deu PAR!!!")
        if p_i == 'p':
            print('Você ganhou!!!')
            win += 1
        else:
            print("Você perdeu!!!")
            print('')
            print('Fim de Jogo!!!')
            print('')
            print(f"<<<Você jogou {count} vezes e ganhou {win} vezes>>> ")
            break
    else:
        print("Deu ÍMPAR!!!")
        if p_i == 'i':
            print('Você ganhou!!!')
            win += 1 
        else:
            print("Você perdeu!!!")
            print('')
            print("Fim de Jogo!!!")
            print('')
            print(f"<<<Você jogou {count} vezes e ganhou {win} vezes>>>")
            break
    print('')
    
    
