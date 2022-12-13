from Drink import Drink


class HotDrink(Drink):
    def __init__(self, name, volume, temperature):
        super().__init__(name, volume)
        self.temperature = temperature

    def __str__(self):
        return f"{self.name}, {self.volume}, {self.temperature}"
