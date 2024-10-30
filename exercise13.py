# João precisa calcular seu Índice de Massa Corporal (IMC) para avaliar seu peso ideal. Sabendo que a fórmula para calcular o IMC é: peso ÷ altura², crie um programa que calcule e informe a classificação do IMC.

def imc(peso, altura):
    calculoImc = peso/(altura*altura)
    if (calculoImc <= 18.5):
        return "Magreza"
    elif (calculoImc > 18.5) and (imc <= 24.9):
        return "Saudavel"
    elif (calculoImc >= 25) and (imc <= 29.9):
        return "Sobrepeso"
    elif (calculoImc > 30) and (imc <= 34.9):
        return "Obesidade grau 1"
    elif (calculoImc > 35) and (imc <= 39.9):
        return "Obesidade severa grau 2"
    else:
        return "Obesidade morbida grau 3"


peso = 50
altura = 160

imcJoao = imc(peso, altura)
print("O IMC do João é ", imcJoao)
