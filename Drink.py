class Drink:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def __str__(self):
        return f"{self.name}, {self.volume}"
