# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=npmodif
def npmodif(n, a, b):
    '''on va créer une arange(n) et transformer
    en leurs opposés les termes d'indices compris entre a et b.
    La fonction retourne le tableau np modifié'''
    import numpy as np
    Z = np.arange(n)
    Z[(a < Z) & (Z <= b)] *= -1
    return list(Z)
# @END@



inputs_npmodif = [
    Args(10, 3, 5),
    Args(10, 2, 8),
    Args(5, 1, 3),
    Args(15, 10, 14),
    
]



exo_npmodif = ExerciseFunction(
    npmodif, inputs_npmodif)
