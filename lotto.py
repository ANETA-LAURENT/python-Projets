""" Ecrivez un programme pour simuler le lotto. Le programme implémente une liste de 7 nombres, qui représente
un ticket de lotto. Le programme va ensuite générer 7 nombres aléatoires et comparer au ticket.
Le programme affiche ensuite la somme gagnée en suivant les règles ci dessous (en fonction de combien de
nombres correspondent entre le ticket et les nombres tirés)● 20 euros si 3 nombres correspondent """

import random as r


def lotto():

    pull = list(range(1, 49))
    pull_set = set(range(1, 50))
    tirage = r.sample(pull, 7)

    input_numbers = input("Choisissez 7 numéros entre 1 à 49 separés avec une espace: ")

    count_numbers = str(input_numbers).split()

    if len(count_numbers) != 7:
        print("Vous devrez choisir 7 numéros.")

    else:
        my_choice = list(map(int, input_numbers.strip().split()))[:7]

        mine_choice = set(my_choice)

        if pull_set.intersection(mine_choice):

            intersection = set(tirage).intersection(mine_choice)

            result = len(intersection)

            if result == 3:
                print(
                    f"Vous avez trouvez {result} bons numeros :{intersection}. Vous gagnez 20 euro"
                )
            elif result == 4:
                print(
                    f"Vous avez trouvez {result} bons numeros :{intersection}. Vous gagnez 40 euro"
                )
            elif result == 5:
                print(
                    f"Vous avez trouvez {result} bons numeros :{intersection}. Vous gagnez 100 euro"
                )
            elif result == 6:
                print(
                    f"Vous avez trouvez {result} bons numeros :{intersection}. Vous gagnez 10 000 euro"
                )
            elif result == 7:
                print(
                    f"Vous avez trouvez {result} bons numeros :{intersection}. Vous gagnez 1 000 000 pour 7 nombres"
                )

            else:
                print("Vous avez perdu ")
        else:
            ("too big")

        print(sorted(tirage))
        print(type(mine_choice))


lotto()
