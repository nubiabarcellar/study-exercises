# Exercício 4: Fatorial de um número
# Escreva um programa que receba um número inteiro do usuário e calcule o fatorial desse número.

import math


class Factorial:
    def __init__(self, num: int):
        self.num = num

    def calculate_factorial(self) -> int:
        return math.factorial(self.num)


def main():
    num_input = int(input("Digite um número para calcular seu fatorial: "))

    factorial_calculated = Factorial(num_input)

    print("O fatorial do número ", num_input, " é ",
          factorial_calculated.calculate_factorial())


if __name__ == "__main__":
    main()