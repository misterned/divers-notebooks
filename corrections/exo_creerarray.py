# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=creerarray
def creerarray(n):
    '''une fonction qui crée un tableau
    tab[i, j] = i**2 + 10 * j'''
    import numpy as np
    ix, iy = np.indices((n, n))
    tab = ix**2 + 10 * iy
    return tab[n-1,n-1]
# @END@



inputs_creerarray = [
    Args(5),
    Args(6),
    Args(7),
    Args(8),
    
]



exo_creerarray = ExerciseFunction(
    creerarray, inputs_creerarray)
