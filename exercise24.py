# Exercício 5: Ordenar uma lista
# Escreva um programa que receba uma lista de números do usuário e exiba a lista ordenada em ordem crescente.

from typing import List


class ListOrder:
    def __init__(self, mumbers_list: List[int]):
        self.mumbers_list = mumbers_list

    def sort_list(self) -> List[int]:
        return sorted(self.mumbers_list)


def main():
    list_input = input(
        "Digite uma lista de números separados por vírgula para que ela seja ordenada em ordem crescente: ")

    unordered_list = [int(num.strip()) for num in list_input.split(',')]

    ordered_list = ListOrder(unordered_list)

    print(f"Segue a lista {unordered_list} ordenada em ordem crescente: {ordered_list.sort_list()}")


if __name__ == '__main__':
    main()
