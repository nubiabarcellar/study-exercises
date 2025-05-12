#Exercício 2: Verificar se um número é par ou ímpar
#Escreva um programa que receba um número do usuário e informe se ele é par ou ímpar.

print("Digite um número e descubra se ele é par ou impar:")
num = int(input())

if(num % 2 == 0):
    print("O número é par!")
else:
    print("O número é impar!")