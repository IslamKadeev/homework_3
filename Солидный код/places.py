from abc import ABC, abstractmethod


class Place(ABC):
    @abstractmethod
    def find_enemy(self):
        pass


class Kostroma(Place):
    name = 'Kostroma'

    def find_enemy(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def find_enemy(self):
        print('Godzilla stands near a skyscraper')
