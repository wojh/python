# 63 - Escreva um programa que leia um número n inteiro qualquer
# e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

#0  ==>
#1  ==> 0
#2  ==> 0, 1 
#3  ==> 0, 1, 1 
#4  ==> 0, 1, 1, 2
#5  ==> 0, 1, 1, 2, 3 
#6  ==> 0, 1, 1, 2, 3, 5
#7  ==> 0, 1, 1, 2, 3, 5, 8 
#8  ==> 0, 1, 1, 2, 3, 5, 8, 13
#9  ==> 0, 1, 1, 2, 3, 5, 8, 13, 21
#10 ==> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

n = int(input("Tecle Quantos números da Sequência de Fibonacci deseja: "))
print('')
print(f"Segue abaixo, os {n} primeiros números da Sequência de Fibonacci")
print('')

if n == 1:
    print(0)
elif n == 2:
    print(0, 1)
elif n ==3:
    print(0, 1, 1)
elif n>3:
    print(0)
    print(1)
    print(1)
    count = 2   
    fib_anterior = 1 
    fib_atual = 1 
    fib = fib_atual + fib_anterior
    while count < n:
        print(fib)
        count += 1 
        fib_anterior = fib_atual
        fib_atual = fib 
        fib = fib_anterior + fib_atual
    
    
    
    
    
    
    
    
    
    
