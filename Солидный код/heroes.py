from antagonistfinder import AntagonistFinder
from weapons import Weapons

class SuperHero(Weapons):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        self.fire_a_gun()

    def ultimate(self):
        pass


class ChakNorris(SuperHero, Weapons):
    def __init__(self):
        super(ChakNorris, self).__init__('Chak Norris', False)


class Superman(SuperHero, Weapons):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        return Weapons.kick()
