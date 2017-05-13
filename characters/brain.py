from characters.strategy import Strategy
import numpy.random as npr

METRICS = lambda one, two: ((one.x - two.x) + (one.y - two.y))  ** (0.5)
init = ['move', 'attack', 'pass']
class Brain():
    def __init__(self, decisions=init, identifier=0):
        self.identifier = identifier
        self.strategies = {'init': Strategy(loss=lambda x: x, decisions=decisions)}

    def decide(self, npc, world, strategy_name='init'):
        dec_list = self.strategies[strategy_name].decide(npc, world)

        #eval_loss = self.strategies[strategy_name].loss(npr.rand() * 2 - 1)
        #self.strategies[strategy_name].dec_weights[dec_list] += eval_loss
        return dec_list
        # print(dec_list, self.strategies[strategy_name].dec_weights[dec_list])