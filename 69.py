# 69 - Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final mostre:
# a - quantas pessoas tem mais de 18 anos;
# b - quantos homens foram cadastrados;
# c - quantas mulheres tem menos de 20 anos.
count = mens = womans = id_18 = int(0)
while True:
    n = int(input('Qual sua idade?? ')) 
    s = input("Masculino ou Feminino [M/F]: ")
    while s != 'm' and s != 'f':
        s = input("Masculino ou Feminino [M/F]: ")
        
    print('')
    if n>18:
        id_18 += 1
    
    if s == 'm':
        mens += 1
    
    if n<20 and s == 'f':
        womans += 1
    
    count += 1 
    
    start_end = input("Deseja continuar [s/n] ?? ").lower()
    
    if start_end == 'n':
        break
    print('')
    
print(f"""Foram cadastrados {id_18} pessoas com mais de 18 anos.
Além disso, foram cadastrados {mens} homens e {womans} mulheres com menos de 20 anos!!!""")
