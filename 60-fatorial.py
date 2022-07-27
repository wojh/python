# 60 - Faça um programa que leia um número qualquer e mostre o seu 
# fatorial. Com while e com for.


n = int(input("Insira o número inteiro: "))
print('')

# Com while

if n == 0 or n == 1:
    print(f"O fatorial de {n} é 1.")
elif n>1:
    count = (n - 1)
    fat = n*count
    count -= 1 
    while count>1:
        fat *= count
        count -= 1 
    print(f'O fatorial é {fat}')


# Com for

if n == 0 or n == 1:
    print(f"O fatorial de {n} é 1.")
elif n>1:
    fat = n
    for c in range(n-1, 1, -1):
        fat = fat*c
    print(f'O fatorial é {fat}')
    
