
def CALCULE_AGE():
    ANN_NAISS = int(input(("Entrez votre année de naissance:\n")))
    ann_actuel = 2025

    print(f"Vous avez {ann_actuel - ANN_NAISS} ans")

    if ANN_NAISS - ann_actuel < 20:
        print(f"Vous êtes plutôt jeune")
    else:
        print(f"Vous n'êtes pas si jeune")


CALCULE_AGE()
