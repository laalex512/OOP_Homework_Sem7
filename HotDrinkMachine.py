from VendingMachine import VendingMachine


class HotDrinkMachine(VendingMachine):

    def saleDrink(self, name, volume, temperature):
        isExist = False
        for i in self.drinksList:
            if i.name == name and i.volume == volume and i.temperature == temperature:
                isExist = True
                super().saleDrink(i)
                print(i.temperature, end = "")
                break
        if not isExist:
            print("No drinks with this parametres")

    def viewMachine(self):
        for i in self.drinksList:
            print(i)
        print()
