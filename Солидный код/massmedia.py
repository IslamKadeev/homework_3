class Media:
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def create_news(self, place):
        place_name = getattr(place, 'name', 'place')
        print(f'{self.name} saved the {place_name}!')
