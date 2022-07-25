#49 -  Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('')
num = int(input('Insira o número inteiro para calcularmos sua tabuada: '))
print(' ')

print(f"Pronto!!! Abaixo segue a tabuada de 0 a 10 de {num}")

for c in range(0,11):
    print(f"{num}*{c} = {c*num}")
