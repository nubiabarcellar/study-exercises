# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.

def calculadora(num1, num2, oper):
    if (oper == 1):
        return num1 + num2
    elif (oper == 2):
        return num1 - num2
    elif (oper == 3):
        return num1 * num2
    elif (oper == 4) and (num2 != 0):
        return num1 / num2
    else:
        return 0


executar = True
while (executar == True):
    print("Escolha uma opção:")
    print("1: Soma 2: Subtração 3: Multiplicação 4: Divisão 0: Sair")
    oper = int(input())
    if (oper < 0) or (oper > 4):
        print("Essa opção não existe")
    elif (oper == 0):
        executar = False
    else:
        print("A opção selecionada foi ", oper)
        print("Agora, digite um número.")
        num1 = int(input())
        print("O primeiro número é ", num1)
        print("Digite outro número.")
        num2 = int(input())
        print("O segundo número é ", num2)
        resultado = calculadora(num1, num2, oper)
        print("O resultado da operação é: ", str(resultado))
