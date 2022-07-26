# 57 - Faça um programa que leia o sexo de uma pessoa, 
# mas só aceite os valores “M” ou “F”. Caso esteja errado, 
# peça a digitação novamente até ter um valor correto.

sex = input("Tecle seu sexo [M/F]: ").upper()

while sex != 'M' and sex != 'F':
    print('')
    print("Tente Novamente!!!")
    sex = input("""Tecle M para MASCULINO ou F para FEMININO: """).upper()

print('')
print('Pronto!!!')
if sex == 'M':
    print('Masculino')
else:
    print("Feminino")
    
