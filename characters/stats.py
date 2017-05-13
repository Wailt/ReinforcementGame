import numpy as np

class Stats:

    def __init__(self):
        # Character's skills
        # Will change (improve) during time
        self.skills = {"fight" : np.random.rand()/10 + 1,
                       "defence" : np.random.rand()/10 + 1,
                       "athletics" : np.random.rand()/10 + 1}

        # Character's attributes
        # Character is born with this values and cannot change them
        self.attributes = {"strength" : np.random.uniform(1, 2),
                           "agility" : np.random.uniform(1, 2),
                           "stamina" : np.random.uniform(1, 2)}

        self.phisics = {"x_velosity" : lambda: self.attributes['athletics'] + self.skills['agility'],
                        "y_velosity" : lambda: self.attributes['athletics'] + self.skills['agility'],
                        "force" : lambda: self.attributes['strength'] + self.skills['fight'],
                        "mass" : lambda: self.attributes['stamina'] + self.skills['defence']}

        self.skills_upgrade = {key : 0 for key in self.skills}