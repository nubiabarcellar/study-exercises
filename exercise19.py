# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

anoAtual = 2022
anoNasc = False

print("Digite seu nome completo.")
nome = str(input())

while (anoNasc == False):
    print("Digite seu ano de nascimento")
    try:
        anoNasc = int(input())
        # if (anoNasc >= 1922 and anoNasc <= 2021):
        #     anoNasc == True
        #     idade = anoAtual - anoNasc
        #     print(nome, "tem", idade, "anos de idade no ano de", anoAtual)
        # else:
        #     print("O ano informado não atende nossos parâmetros.")
        if (anoNasc < 1922 or anoNasc > 2021):
            print("O ano informado não atende nossos parâmetros.")
        else:
            idade = anoAtual - anoNasc
            print(nome, "tem", idade, "anos de idade no ano de", anoAtual)
            anoNasc == True
    except:
        print("Caractere inválido.")
