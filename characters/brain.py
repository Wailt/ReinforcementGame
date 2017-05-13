from characters.strategy import Strategy
import numpy.random as npr

METRICS = lambda one, two: ((one.x - two.x) + (one.y - two.y))  ** (0.5)

class Brain():
    #decisions = ['move', 'attack', 'defence']
    def __init__(self, decisions):
        self.strategies = {'init': Strategy(loss=lambda x: x, decisions=decisions)}

    def decide(self, npc, world, strategy_name='init'):
        name, dec_list = self.strategies[strategy_name].decide(npc, world)
        #ta ta ta
        eval_loss = self.strategies[strategy_name].loss(npr.rand() * 2 - 1)
        self.strategies[strategy_name].dec_weights[name] += eval_loss