# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

# Escreva um código que imprima todos os números exceto o número 13.

import random

andares = 21
for i in range(21):
    andares = andares - 1
    if (andares == 13):
        continue
    if (andares == 0):
        break
    print(andares)

# Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

for i in range(21, 1, -1):
    print(i)

andares = random.randint(1, 21)
while (andares == 21):
    print(andares)
    andares = random.randint(1, 21)

    # Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
