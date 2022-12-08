

import random as rd

puertas = [1, 2, 3]
intentos = 10000
aciertos = 0

for i in range(intentos):

    puerta_auto = rd.choice(puertas)
    puerta_elegida = rd.choice(puertas)
    disponibles = [x for x in puertas if x!= puerta_elegida and x!= puerta_auto]
    opened_doors = rd.sample(disponibles, len(puertas)-2)
    new_choice = [x for x in puertas if x not in opened_doors if x != puerta_elegida][0]

    if puerta_auto ==  new_choice:
        aciertos += 1

score = aciertos / intentos

print(score) 