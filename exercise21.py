# Exercício 2: Verificar se um número é par ou ímpar
# Escreva um programa que receba um número do usuário e informe se ele é par ou ímpar.

class ChecksIfNumberIsEvenOrOdd:
    def __init__(self, num: int):
        self.num = num

    def check_if_number_is_even_or_odd(self) -> str:
        return "par" if (self.num % 2 == 0) else "impar"

num_input = int(input("Digite um número e descubra se ele é par ou impar:"))

number_checked = ChecksIfNumberIsEvenOrOdd(num_input)

print(f"O número ", num_input, " é ", number_checked.check_if_number_is_even_or_odd())