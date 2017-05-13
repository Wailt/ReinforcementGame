import numpy.random as npr
import numpy as np

temperature = 10
class Strategy:
    def __init__(self, loss, decisions=[], n=3):
        self.decisions = decisions
        self.loss = loss
        self.dec_weights = dict()

    def decide(self, npc, world):
        if npr.rand(len(self.dec_weights) + 1):
            dec_list = self.create_new_decs()
        else:
            dec_list = self.choose_dec()

    def create_new_decs(self):
        pass

    def choose_dec(self):
        norma = sum(np.exp(temperature * np.array([self.dec_weights[k] for k in self.dec_weights])))
        level = npr.rand()
        cumsum = 0
        for key in self.dec_weights:
            # TODO: here temperature
            cumsum += np.exp(temperature * self.dec_weights[key]) / norma
            if cumsum >= level:
                pass
#                return {'moove': (key, decision['moove'][key])}
#        return {'moove': ('random', decision['moove'][''])}

