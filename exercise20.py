# Exercício 1: Soma de dois números
# Escreva um programa que receba dois números do usuário e exiba a soma deles.

class SumNumbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add_numbers(self) -> int:
        return self.num1 + self.num2


print("Digite um número: ")
num1 = int(input())
print("Digite outro número: ")
num2 = int(input())

sum_result = SumNumbers(num1, num2)

print("A soma dos números ", num1, " e ",
      num2, " é: ", sum_result.add_numbers())
