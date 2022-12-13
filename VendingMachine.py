
class VendingMachine:

    def __init__(self, name):
        self.name = name
        self.drinksList = []

    def pushDrink(self, drink):
        self.drinksList.append(drink)

    def saleDrink(self, drink):
        if drink in self.drinksList:
            self.drinksList.remove(drink)
            print(f"Saled: {drink.name} {drink.volume} ", end="")
            return drink
        else:
            print("No drinks with this parametres")

    def viewMachine(self):
        for i in self.drinksList:
            print(i)
        print()
