import numpy as np
import numpy.random as npr

temperature = 10


class Strategy:
    def __init__(self, loss, decisions=[], n=3):
        self.decisions = decisions
        self.loss = loss

        # {id: list}
        self.dec_weights = dict()

    def decide(self, npc, world):
        if npr.rand(len(self.dec_weights) + 1):
            name, dec_list = self.create_new_decs()
        else:
            name, dec_list = self.choose_dec()

        return name, dec_list

    def create_new_decs(self):
        dec_list = [self.decisions[i] for i in npr.randint(0, len(self.decisions))]
        while dec_list in self.dec_weights:
            dec_list = [self.decisions[i] for i in npr.randint(0, len(self.decisions))]

        old_len = len(self.dec_weights)
        self.dec_weights[old_len] = dec_list
        return old_len, dec_list

    def choose_dec(self):
        norma = sum(np.exp(temperature * np.array([self.dec_weights[k] for k in self.dec_weights])))
        level = npr.rand()
        cumsum = 0
        for key in self.dec_weights:
            cumsum += np.exp(temperature * self.dec_weights[key]) / norma
            if cumsum >= level:
                return key, self.dec_weights[key]

# return {'moove': ('random', decision['moove'][''])}
