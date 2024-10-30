# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.


def calculadora(num1, num2, oper):
    if (num1 + num2):
        soma = oper
        return soma
    elif oper:
        subt = num1 - num2
        return subt
    elif oper:
        mult = num1 * num2
        return mult
    else:
        divi = num1 / num2
        return divi
    
resultado = calculadora(2,5, soma)
print(resultado)
    

