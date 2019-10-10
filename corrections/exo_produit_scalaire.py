# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=produit_scalaire
def produit_scalaire(X, Y):
    """
    retourne le produit scalaire
    de deux listes de même taille
    """
    # on utilise la fonction builtin sum sur une itération
    # des produits x*y 
    # avec zip() on peut faire correspondre les X avec les Y
    # remarquez bien qu'on utilise ici une expression génératrice
    # et PAS une compréhension car on n'a pas du tout besoin de
    # créer la liste des produits x*y 
    return sum(x * y for x, y in zip(X, Y))
# @END@


# @BEG@ name=produit_scalaire more=bis
# Il y a plein d'autres solutions qui marchent aussi
def produit_scalaire_bis(X, Y):
    # initialisation du résultat
    scalaire = 0
    for x, y in zip(X, Y):
        scalaire += x * y
    # on retourne le résultat
    return scalaire
# @END@


# @BEG@ name=produit_scalaire more=ter
# et encore une: celle-ci par contre est assez peu "pythonique"
# je la donne plutôt comme un exemple de ce qu'il faut éviter
# on aime bien en général éviter les boucles du genre
# for i in range(len(iterable)):
#     ... iterable[i]
def produit_scalaire_ter(X, Y):
    scalaire = 0
    n = len(X)
    for i in range(n):
        scalaire += X[i] * Y[i]
    return scalaire
# @END@


from fractions import Fraction


inputs_produit_scalaire = [
    Args((1, 2), (3, 4)),
    Args(range(3, 9), range(5, 11)),
    Args([-2, 10], [20, 4]),
    Args([Fraction(2, 15), Fraction(3, 4)], [
         Fraction(-7, 19), Fraction(4, 13)]),
    Args([], []),
]


exo_produit_scalaire = ExerciseFunction(
    produit_scalaire,
    inputs_produit_scalaire,
)


def produit_scalaire_ko(X, Y):
    return [x * y for x, y in zip(X, Y)]


