# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(num1, num2, oper):
    if (oper == 1):
        return num1 + num2
    if (oper == 2):
        return num1 - num2
    if (oper == 3):
        return num1 * num2
    if (oper == 4):
        return num1 / num2
    else:
        return 0

resultado = calculadora(5, 2, 4)
print(resultado)