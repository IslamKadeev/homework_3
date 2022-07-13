class Gun:
    @staticmethod
    def fire_a_gun():
        print('PIU PIU')


class Laser:
    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


class MartialArt:
    @staticmethod
    def roundhouse_kick():
        print('Bump')

    @staticmethod
    def kick():
        print('Kick')


class Weapons(Gun, Laser, MartialArt):
    pass
