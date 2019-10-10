# -*- coding: utf-8 -*-
from nbautoeval.exercise_class import ExerciseClass, ScenarioClass
from nbautoeval.args import Args

# @BEG@ name=fifo
class Fifo:
    """
    Une classe FIFO implémentée avec une simple liste
    """
    
    def __init__(self):
        # l'attribut queue est un objet liste
        self.queue = []

    def incoming(self, x):
        # on insère au début de la liste
        self.queue.insert(0, x)

    def outgoing(self):
        # une première façon de faire consiste à
        # utiliser un try/except
        try:
            return self.queue.pop()
        except IndexError:
            return None
# @END@


# @BEG@ name=fifo more=bis
class FifoBis(Fifo):
    """
    une alternative en testant directement
    plutôt que d'attraper l'exception
    """
    def __init__(self):
        self.queue = []

    def incoming(self, x):
        self.queue.insert(0, x)

    def outgoing(self):
        # plus concis mais peut-être moins lisible
        if len(self.queue):
            return self.queue.pop()
        # en fait on n'a même plus besoin du else..

# @END@ 

fifo_scenarios = [
    ScenarioClass(
        # init arguments
        Args(),
        'outgoing', Args(),
        'incoming', Args(1),
        'incoming', Args(2),
        'outgoing', Args(),
        'outgoing', Args(),
        'outgoing', Args(),
    ),
    ScenarioClass(
        # init arguments
        Args(),
        'incoming', Args(1),
        'incoming', Args(2),
        'outgoing', Args(),
        'incoming', Args(3),
        'outgoing', Args(),
        'outgoing', Args(),
        'outgoing', Args(),
    ),
    
    ScenarioClass(
        # init arguments
        Args(),
        'incoming', Args(1),
        'incoming', Args(2),
        'outgoing', Args(),
        'outgoing', Args(),
        'incoming', Args(3),
        'incoming', Args(4),
        'outgoing', Args(),
        'outgoing', Args(),
    ),

]

exo_fifo = ExerciseClass (
    Fifo, fifo_scenarios,
    layout='pprint'
)

