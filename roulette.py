import random


def color():
    randColor = random.randint(1, 2)

    if randColor == 1:
        resultat = "rouge"
    else:
        resultat = "noir"
    return resultat


def game():
    while True:
        pari = int(input("Vous voulez parier quelle somme?:"))
        compColor = color()
        compNumber = random.randint(1, 2)
        chosenColor = input("Quel couleur: rouge ou noir?:")
        chosenNumber = int(input("Choisissez un nombre entre 1 et 2:"))

        if chosenColor == compColor and chosenNumber != compNumber:

            print(
                f"Vous avez choisi un bon coleur: {compColor} mais pas un bon numero qui a été {compNumber} mais vous gardez quand même votre argent: {pari} euro."
            )

        elif chosenNumber == compNumber and chosenColor != compColor:

            pari = int(pari) * 2
            print(
                f"Vous avez trouvez un bon nombre mais pas un bon couleur, on double votre pari. Vous avez donc gagné {pari} euros."
            )

        elif chosenNumber == compNumber and chosenColor == compColor:
            pari = int(pari)

            print(
                f"Vous avez trouvez le bon couleur et le bon nombre. Vous gagnez 100 fois votre mise donc: {pari} euro"
            )

        else:
            print(
                f"Vous n'avez pas trouvez ni bon couleur ni bon numero. Le couleur demandé a été {compColor} et le numero : {compNumber}. Vous avez perdu!"
            )

        replay = input("Vous voulez rejouer?(oui/non): ")
        if replay == "oui":
            continue
        else:

            print("Alors, à la prochaine")
            break


color()
game()
