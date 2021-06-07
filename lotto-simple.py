import random as r


def lotto():
    print("Pour jouer en lotto choisissez 7 numéros entre 1 à 49: ")
    pull = range(1, 12)
    your_choice = []
    tirage = r.sample(pull, 7)

    while len(your_choice) < 7:
        your_numbers = int(input("Votre numero: "))
        if 1 <= your_numbers <= 12 and your_numbers not in your_choice:
            your_choice.append(your_numbers)

    your_choice.sort()
    tirage.sort()
    result = set(your_choice).intersection(tirage)
    if len(result) == 3:
        print(
            f"Vous avez trouvez {len(result)} bons numeros :{result}. Vous gagnez 20 euro"
        )
    elif len(result) == 4:
        print(
            f"Vous avez trouvez {len(result)} bons numeros :{result}. Vous gagnez 40 euro"
        )
    elif len(result) == 5:
        print(
            f"Vous avez trouvez {len(result)} bons numeros :{result}. Vous gagnez 100 euro"
        )
    elif len(result) == 6:
        print(
            f"Vous avez trouvez {len(result)} bons numeros :{result}. Vous gagnez 10 000 euro"
        )
    elif len(result) == 7:
        print(
            f"Vous avez trouvez {len(result)} bons numeros :{result}. Vous gagnez 1 000 000 euro"
        )

    else:
        print("Perdu")

    print(
        f"Vos numeros:  {sorted(your_choice)} et les numéros gagnants: {sorted(tirage)} "
    )


lotto()