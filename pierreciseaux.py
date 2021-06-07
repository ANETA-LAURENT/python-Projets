import random


def game():
    computerChoice = random.randint(1, 3)

    if computerChoice == 1:
        resultat = "pierre"

    elif computerChoice == 2:
        resultat = "papier"

    else:
        resultat = "ciseaux"
    return resultat


def you():
    myChoice = input("Tu choisi: pierre papier ou ciseaux? ")
    otherChoice = game()
    print(f"Votre adversaire a choisi {otherChoice}")

    if myChoice == otherChoice:
        print("Egalité: personne a gagné.")
        another = input("vous voulez rejouer? (oui/non): ")
        if another == "oui":
            you()
        else:
            print("Bye bye")

    elif myChoice == "ciseaux" and otherChoice == "papier":
        print("Vous avez gagnez!")
    elif myChoice == "papier" and otherChoice == "pierre":
        print("Vous avez gagnez!")

    elif myChoice == "pierre" and otherChoice == "ciseaux":
        print("Vous avez gagnez!")
    else:
        print("Vous avez perdu")


game()
you()