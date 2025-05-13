# Exercício 3: Contar vogais em uma string
# Escreva um programa que receba uma string do usuário e conte quantas vogais existem nela.

class VowelCounter:
    def __init__(self, text: str):
        self.text = text
        self.vowels = ('aeiouAEIOU')

    def count_vowel(self):
        counter = 0

        for letter in self.text:
            if letter in self.vowels:
                counter += 1

        return counter

text_input = str(input("Escreva uma frase para saber quantas vogais ela possui: "))

total_vowel = VowelCounter(text_input)

print("O total de vogais nessa frase é de: ", total_vowel.count_vowel())