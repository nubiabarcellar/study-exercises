# Exercício 7: Gerar uma lista de números pares
# Escreva um programa que receba dois números inteiros (início e fim) e gere uma lista contendo todos os números pares nesse intervalo.

from typing import List

class ListGenerator:
    def __init__(self, start_number: int, end_number: int):
        self.start_number = start_number
        self.end_number = end_number

    def generate_list(self) -> list:
        list_of_even_numbers = []

        for number in range(self.start_number, self.end_number):
            if number % 2 == 0:
                list_of_even_numbers.append(number)

        return list_of_even_numbers

def main():
    start_number = int(input("Digite o primeiro número da lista: "))
    end_number = int(input("Digite o último número da lista: "))
    
    generate_even = ListGenerator(start_number, end_number)

    print(f"A lista de números pares do intervalo é: ", generate_even.generate_list())

if __name__ == '__main__':
    main()