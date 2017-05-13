import numpy as np
import numpy.random as npr

temperature = 10


class Strategy:
    def __init__(self, loss, decisions=[], n=3):
        self.decisions = decisions
        self.loss = loss
        self.size = n
        # {id: list}
        self.dec_weights = dict()

    def decide(self, npc, world):
        if len(self.dec_weights) < len(self.decisions) ** self.size:
            if not npr.randint(len(self.dec_weights) + 1):
                dec_list = self.create_new_decs()
            else:
                dec_list = self.choose_dec()
        else:
            return self.choose_dec()

        return dec_list

    def create_new_decs(self):
        dec_list = tuple([self.decisions[i] for i in npr.randint(0, len(self.decisions), self.size)])
        while dec_list in self.dec_weights:
            dec_list = tuple([self.decisions[i] for i in npr.randint(0, len(self.decisions), self.size)])
        self.dec_weights[dec_list] = 0
        return dec_list

    def choose_dec(self):
        norma = sum(np.exp(temperature * np.array([self.dec_weights[k] for k in self.dec_weights])))
        level = npr.rand()
        cumsum = 0
        for key in self.dec_weights:
            cumsum += np.exp(temperature * self.dec_weights[key]) / norma
            if cumsum >= level:
                return key
        return list(self.dec_weights.keys())[0]


# return {'moove': ('random', decision['moove'][''])}
