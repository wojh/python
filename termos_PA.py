#50 - 51 - Programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.



a1 = int(input("Insira o primeiro termos da PA:"))
print('')
r = int(input("Pronto!!! Agora insira a razão da PA: "))
print("")
print("Show!!! Abaixo segue os 10 primeiros da PA!!!")

n = int(10)

termos = []

for c in range(a1, a1 + (n-1)*r + r , r):
    termos += [c]
 
print(f"{termos}", end='')
print(' ')
print(len(termos))

