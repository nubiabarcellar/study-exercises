# Desenvolva um programa que só deve aceitar números pares. Siga as seguintes instruções:

# caso um número ímpar seja digitado, informe ao usuário que ele digitou um valor ímpar e peça novamente por um número par;

# caso uma letra seja digitada, informe ao usuário que ele digitou um caractere inválido e peça novamente por um número par.

numeroPar = False

while (numeroPar == False):
    print("Insira um número par.")
    try:
        numero = int(input())
        if (numero % 2 == 0):
            numeroPar = True
            print("O número par digitado foi: ", numero)
        else:
            print("O número digitado é impar.")
    except:
        print("Caractere inválido.")
