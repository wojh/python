# 70 - Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# a - qual é o total gasto na compra;
# b - quantos produtos custam mais de R$1000,00;
# c - qual é o nome do produto mais barato.

valor_gasto = float(0)
count = int(0)

nome = input("Digite o nome do produto: ")
preço = float(input("Agora o preço dele: "))
valor_gasto += preço
valor_barato = preço
produto_barato = nome 

if preço > 1000:
    count +=1 

end = input("Deseja continuar [s/n]: ")
while end!='s' and end!='n':
    end = input("Deseja continuar [s/n]: ")

while end == 's':
    print('')
    nome = input("Digite o nome do produto: ")
    preço = float(input("Agora o preço dele: "))
    valor_gasto += preço
    
    if preço > 1000:
        count +=1 
    
    if valor_barato > preço:
        valor_barato = preço
        produto_barato = nome
    
    print('')
    
    end = input("Deseja continuar [s/n]: ")
    
    while end!='s' and end!='n':
        end = input("Deseja continuar [s/n]: ")
    
    if end == 'n':
        break
    
print("")
print(f"Total da compra: R${valor_gasto:.2f}")

if count == 0:
    print("Nenhum produto custa mais de R$1000.00")
elif count == 1:
    print("1 produto custa mais de R$1000.00")
elif count>1:
    print(f"{count} produtos custam mais de R$1000.00")
print(f"Produto mais barato foi {produto_barato}")
