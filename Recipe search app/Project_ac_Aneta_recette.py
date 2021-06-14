"""
Un programme pour chercher des recettes à partir d'ingrédients. Le projet de base utilise l’API de recettes (en anglais) Edamam,
Note: comme l’API est en anglais, les ingrédients et recettes seront aussi en anglais.
Notre algortihme vous propose 3 recettes contenant les ingrédients que vous avez choisis.Il est possible d'affiner sa recherche par:
- le nombre maxium d'ingerdints utilisés dans la recette,
- par type de repas: petit déjeuner, déjeuner, gouter, ou dinner,
- mais aussi par  critère d'alimentation, ex: vegan, sans noix, sans oeuf, sans oléagineux, sans alcool, sans gluten...
Les résultats de la recherche s'affichent automatiquement dans le navigateur internet et et dans le dossier txt.
"""


import requests
import webbrowser
import secrets

app_id = secrets.app_id
app_key = secrets.app_key

# Search functions
def cherche_recette(ingredient, ingr):
    resultat = requests.get(
        "https://api.edamam.com/search?q={}&ingr={}&app_id={}&app_key={}".format(
            ingredient, ingr, app_id, app_key
        )
    )
    data = resultat.json()
    print(data)
    return data["hits"]


def cherche_recette_meal(ingredient, ingr, mealType):
    resultat = requests.get(
        "https://api.edamam.com/search?q={}&ingr={}&mealType={}&app_id={}&app_key={}".format(
            ingredient, ingr, mealType, app_id, app_key
        )
    )
    data = resultat.json()
    return data["hits"]


def cherche_recette_healthy1(ingredient, ingr, choix1):
    resultat = requests.get(
        "https://api.edamam.com/search?q={}&ingr={}&health={}&app_id={}&app_key={}".format(
            ingredient, ingr, choix1, app_id, app_key
        )
    )
    data = resultat.json()
    return data["hits"]


def cherche_recette_healthy2(ingredient, ingr, choix1, choix2):
    resultat = requests.get(
        "https://api.edamam.com/search?q={}&ingr={}&health={}&health={}&app_id={}&app_key={}".format(
            ingredient, ingr, choix1, choix2, app_id, app_key
        )
    )
    data = resultat.json()
    return data["hits"]


def cherche_recette_healthy3(ingredient, ingr, choix1, choix2, choix3):
    resultat = requests.get(
        "https://api.edamam.com/search?q={}&ingr={}&health={}&health={}&health={}&app_id={}&app_key={}".format(
            ingredient, ingr, choix1, choix2, choix3, app_id, app_key
        )
    )
    data = resultat.json()
    return data["hits"]


def cherche_recette_healthy4(ingredient, ingr, mealType, choix1):
    resultat = requests.get(
        "https://api.edamam.com/search?q={}&ingr={}&mealType={}&health={}&app_id={}&app_key={}".format(
            ingredient, ingr, mealType, choix1, app_id, app_key
        )
    )
    data = resultat.json()
    return data["hits"]


def cherche_recette_healthy5(ingredient, ingr, mealType, choix1, choix2):
    resultat = requests.get(
        "https://api.edamam.com/search?q={}&ingr={}&mealType={}&health={}&health={}&app_id={}&app_key={}".format(
            ingredient, ingr, mealType, choix1, choix2, app_id, app_key
        )
    )
    data = resultat.json()
    return data["hits"]


def cherche_recette_healthy6(ingredient, ingr, mealType, choix1, choix2, choix3):
    resultat = requests.get(
        "https://api.edamam.com/search?q={}&ingr={}&mealType={}&health={}&health={}&health={}&app_id={}&app_key={}".format(
            ingredient,
            ingr,
            mealType,
            choix1,
            choix2,
            choix3,
            app_id,
            app_key,
        )
    )
    data = resultat.json()
    return data["hits"]

######### Main function of the program
def run():
    print(
        "Bienvenue dans l'application qui permet de trouver une recette parfaite pour vous."
    )
######### For loop to chose the number of ingredients

    chosen_nb = []
    stock = int(input("Combien d'ingredients minimum souhaitez-vous utiliser?: "))
    for i in range(stock):
        question = input("Entrez un ingrédient (en anglais): ")
        chosen_nb.append(question)
        ingredient = ",".join(str(e) for e in chosen_nb)

    ingr = int(input("Combien des ingredients maximum voulez vous?: "))
    
    ######### Possibility of healthy option of the meal and thr type of the meal 
    mealType_question = input(
        "Voulez-vous choisir un type de repas ex. dinner? oui/non "
    )
    health_question = input("Voulez vous une recette healthy? oui/non ")
    with open("mycookbook.txt", "w") as fichier:
        # the results are registered in txt file
        if mealType_question == "non" and health_question == "non":

            resultats = cherche_recette(ingredient, ingr)[:3]
            i = 0    #the results are classified with a list from 1 to 3 
            for resultat in resultats:
                i += 1
                recette = resultat["recipe"]
                name = recette["label"]
                nb_ingrs = str(len(recette["ingredients"]))
                nb_servings = str(int(recette["yield"]))
                url = recette["url"]
                text = f"La recette {name} est prevue pour {nb_servings} personnes, elle contient en total {nb_ingrs} ingredients dont: {ingredient}. Vous la trouver sur cette page: {url} \n\n"
                text_to_print = str(i) + ". " + text
                fichier.write(text_to_print)
                webbrowser.open_new(url) #the results will be showed in a browser- 3 widows opened

        elif mealType_question == "oui" and health_question == "non":
            mealType = input(
                "Vous voulez une recette pour breakfast,lunch, dinner, or snack?: "
            )
            resultats = cherche_recette_meal(ingredient, ingr, mealType)[:3]
            for resultat in resultats:
                recette = resultat["recipe"]
                name = recette["label"]
                nb_ingrs = str(len(recette["ingredients"]))
                nb_servings = str(int(recette["yield"]))
                url = recette["url"]
                text = f"La recette {name} est prevue pour {nb_servings} personnes, elle contient en total {nb_ingrs} ingredients dont: {ingredient} est elle est prevue pour  {mealType}. Vous la trouver sur cette page: {url} \n\n"
                fichier.write(text)

                webbrowser.open_new(url)

        elif mealType_question == "non" and health_question == "oui":
            nombre_choix = int(
                input(
                    "Combien de critères santé souhaitez-vous choisir? (entre 1 et 3) \n Liste: alcohol-free, immuno-supportive, celery-free, crustacean-free, dairy-free, egg-free, fish-free, fodmap-free, gluten-free, keto-friendly, kidney-friendly, kosher, low-potassium, lupine-free, mustard-free, \n low-fat-abs, No-oil-added, low-sugar, paleo, peanut-free, pecatarian, pecatarian, pork-free, red-meat-free, sesame-free, shellfish-free, soy-free, sugar-conscious, tree-nut-free, vegan, vegetarian, wheat-free. \n  Nombre de critères à prendre en compte: "
                )
            )
            nombre_choix2 = nombre_choix

            choix_sante = []
            while nombre_choix2 > 0:
                choix = str(input("Ecrivez un critère santé? "))
                choix_sante.append(choix)
                nombre_choix2 -= 1

            if nombre_choix == 1:
                choix1 = choix_sante[0]
                resultats = cherche_recette_healthy1(ingredient, ingr, choix1)[:3]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = f"La recette {name} est prevue pour {nb_servings} personnes, elle contient en total {nb_ingrs} ingredients dont: {ingredient} est elle est {choix1}. Vous la trouver sur cette page: {url} \n\n"
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)

            if nombre_choix == 2:
                choix1 = choix_sante[0]
                choix2 = choix_sante[1]
                resultats = cherche_recette_healthy2(ingredient, ingr, choix1, choix2)[
                    :3
                ]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = f"La recette {name} est prevue pour {nb_servings} personnes, elle contient en total {nb_ingrs} ingredients dont: {ingredient} est elle est {choix1}, {choix2}. Vous la trouver sur cette page: {url} \n\n"
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)

            if nombre_choix == 3:
                choix1 = choix_sante[0]
                choix2 = choix_sante[1]
                choix3 = choix_sante[2]
                resultats = cherche_recette_healthy3(
                    ingredient, ingr, choix1, choix2, choix3
                )[:3]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = f"La recette {name} est prevue pour {nb_servings} personnes, elle contient en total {nb_ingrs} ingredients dont: {ingredient} est elle est {choix1}, {choix2} et {choix3}. Vous la trouver sur cette page: {url} \n\n"
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)

        elif mealType_question == "oui" and health_question == "oui":
            mealType = input(
                "Vous voulez une recette pour breakfast, lunch, dinner, or snack? "
            )

            nombre_choix = int(
                input(
                    "Combien de critères santé souhaitez-vous choisir? (entre 1 et 3) \n Liste: alcohol-free, immuno-supportive, celery-free, crustacean-free, dairy-free, egg-free, fish-free, fodmap-free, gluten-free, keto-friendly, kidney-friendly, kosher, low-potassium, lupine-free, mustard-free, \n low-fat-abs, No-oil-added, low-sugar, paleo, peanut-free, pecatarian, pecatarian, pork-free, red-meat-free, sesame-free, shellfish-free, soy-free, sugar-conscious, tree-nut-free, vegan, vegetarian, wheat-free. \n  Nombre de critères à prendre en compte: "
                )
            )
            nombre_choix2 = nombre_choix
            choix_sante = []
            while nombre_choix2 > 0:
                choix = str(input("Ecrivez un critère santé? "))
                choix_sante.append(choix)
                nombre_choix2 -= 1

            if nombre_choix == 1:
                choix1 = choix_sante[0]
                resultats = cherche_recette_healthy4(
                    ingredient, ingr, mealType, choix1
                )[:3]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = f"La recette {name} est prevue pour {nb_servings} personnes, elle contient en total {nb_ingrs} ingredients dont: {ingredient} est elle est {choix1} et elle est prevue pour {mealType}. Vous la trouver sur cette page: {url} \n\n"
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)

            if nombre_choix == 2:
                choix1 = choix_sante[0]
                choix2 = choix_sante[1]
                resultats = cherche_recette_healthy5(
                    ingredient, ingr, mealType, choix1, choix2
                )[:3]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = f"La recette {name} est prevue pour {nb_servings} personnes, elle contient en total {nb_ingrs} ingredients dont: {ingredient} est elle est {choix1}, {choix2} et elle est prevue pour {mealType}. Vous la trouver sur cette page: {url} \n\n"
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)

            if nombre_choix == 3:
                choix1 = choix_sante[0]
                choix2 = choix_sante[1]
                choix3 = choix_sante[2]
                resultats = cherche_recette_healthy6(
                    ingredient, ingr, mealType, choix1, choix2, choix3
                )[:3]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = f"La recette {name} est prevue pour {nb_servings} personnes, elle contient en total {nb_ingrs} ingredients dont: {ingredient} est elle est {choix1} ,{choix2}, {choix3} et elle est prevue pour {mealType}. Vous la trouver sur cette page: {url} \n\n"
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)
        print(
            "Merci. Vous pouvez trouver les resultats de votre recherche dans le fichier mycookbook.txt "
        )


run()
