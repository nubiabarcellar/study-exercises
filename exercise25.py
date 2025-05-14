# Exercício 6: Verificar se uma palavra é um palíndromo
# Escreva um programa que receba uma palavra do usuário e verifique se ela é um palíndromo (lê-se da mesma forma de trás para frente).

class Palindrome:
    def __init__(self, word: str):
        self.word = word.lower()

    def check_palindrome(self) -> bool:
        return self.word == self.word[::-1]


def main():
    word_to_check = (
        str(input("Digite uma palavra para verificar se ela é um palíndromo: ")))
    word_checked = Palindrome(word_to_check)

    if word_checked.check_palindrome():
        print(f"A palavra {word_to_check} é palíndromo.")
    else:
        print(f"A palavra {word_to_check} não é palíndromo.")

if __name__ == '__main__':
    main()