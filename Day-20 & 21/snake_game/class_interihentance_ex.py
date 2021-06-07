class Animals:
    def __init__(self):
        self.eyes = 2
        self.legs = 4
        self.ears = 2

    def food(self):
        print("Omnivorous")

    def land_habitat(self):
        print("lives in land")

    def water_habitat(self):
        print("lives in water")

    def both_habitat(self):
        print("lives both in land & water")


class Fish(Animals):

    def __init__(self):
        super().__init__()

    def habitat(self):
        super().water_habitat()


class Crocodile(Fish):

    def __init__(self):
        super().__init__()

    def behavior(self):
        super().food()
        super().both_habitat()


croc = Crocodile()
croc.habitat()
croc.behavior()
