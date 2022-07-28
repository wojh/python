# 67 - Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o
# número solicitado for negativo.
while True:
    print("Para parar, tecle um número negativo!!!")
    n = int(input("Insira um número inteiro: "))
    print('')
    if n>=0:
        print(f'Abaixo a tabuada de 0 a 10 de {n}')
        for c in range(0, 11):
            print(f'{n}*{c} = {n*c}')
        print('')
    else:
        break
            
print("Fim do programa!!!")
