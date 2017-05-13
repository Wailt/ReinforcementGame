
class Strategy:
    def __init__(self, loss, decisions=[]):
        self.decisions = decisions
        self.loss = loss
        self.dec_weights = dict()

