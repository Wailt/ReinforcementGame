from characters.strategy import Strategy


METRICS = lambda one, two: ((one.x - two.x) + (one.y - two.y))  ** (0.5)

class Brain():
    #decisions = ['move', 'attack', 'defence']
    def __init__(self, decisions):
        self.strategies = {'init': Strategy(loss=lambda x: x, decisions=decisions)}


    def decide(self, npc, world, strategy_name='init'):
        self.strategies[strategy_name].decide(npc, world)