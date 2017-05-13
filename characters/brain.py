from characters.strategy import Strategy


class Brain():
    def __init__(self, decisions):
        self.strategies = {'init': Strategy(loss=lambda x: x, decisions=decisions)}
