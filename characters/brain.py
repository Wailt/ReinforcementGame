from characters.strategy import Strategy
import numpy.random as npr
TEMP = 100
METRICS = lambda one, two: ((one.x - two.x) + (one.y - two.y))  ** (0.5)
init = ['move', 'attack', 'pass']
class Brain():
    def __init__(self, decisions=init, identifier=0):
        self.identifier = identifier
        self.strategies = {'init': Strategy(loss=lambda x: x, decisions=decisions)}

    def decide(self, npc, world, strategy_name='init'):
        dec_list = self.strategies[strategy_name].decide(npc, world)
        self.last = dec_list
        return dec_list


    def count_loss(self, res, strategy_name):
        #self.strategies[strategy_name].loss
        eval_loss = self.strategies[strategy_name].loss(res)
        self.strategies[strategy_name].dec_weights[self.last] += eval_loss / TEMP
        for key in self.strategies[strategy_name].dec_weights:
            self.strategies[strategy_name].dec_weights[key] *= 0.9999
