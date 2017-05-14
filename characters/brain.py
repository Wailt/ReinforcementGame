from characters.strategy import Strategy
import numpy as np
TEMP = 100
METRICS = lambda one, two: np.abs([(one.x - two.x), (one.y - two.y)])
init = ['move', 'attack', 'pass']
class Brain():
    def __init__(self, decisions=init, identifier=0, n=3):
        self.identifier = identifier
        self.strategies = {False: Strategy(loss=lambda x: x, decisions=decisions, n=n),
                           True: Strategy(loss=lambda x: -x/2, decisions=decisions, n=max(n - 1, 1))}

    def decide(self, npc, world, strategy_name='init'):
        dec_list = self.strategies[strategy_name].decide(npc, world)
        self.last = dec_list
        return dec_list


    def count_loss(self, res, strategy_name):
        eval_loss = self.strategies[strategy_name].loss(res)
        self.strategies[strategy_name].dec_weights[self.last] += eval_loss / TEMP
        for key in self.strategies[strategy_name].dec_weights:
            self.strategies[strategy_name].dec_weights[key] *= 0.8
