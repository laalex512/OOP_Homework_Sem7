from Drink import Drink
from HotDrink import HotDrink
from VendingMachine import VendingMachine
from HotDrinkMachine import HotDrinkMachine
from Utils import Utils as UI


def startProgram():

    # Холодные напитки:
    water = Drink("water", 1.0)
    mineralWater = Drink("MinWater", 0.5)
    sparklingWater = Drink("SparkWater", 0.5)
    coldMachine = VendingMachine("Cold Machine")
    for i in range(2):
        UI.pushDrink(coldMachine, water)
        UI.pushDrink(coldMachine, mineralWater)
        UI.pushDrink(coldMachine, sparklingWater)

    UI.showMachine(coldMachine)
    UI.saleAllDrink(coldMachine, water)
    print()
    UI.saleAllDrink(coldMachine, water)
    print()
    UI.saleAllDrink(coldMachine, water)
    print()
    UI.showMachine(coldMachine)

    # Горячие напитки
    cofee = HotDrink("cofee", 0.2, 60)
    tea = HotDrink("tea", 0.3, 50)
    fruitTea = HotDrink("fruitTea", 0.3, 40)
    hotMachine = HotDrinkMachine("Hot Machine")

    for i in range(2):
        UI.pushDrink(hotMachine, cofee)
        UI.pushDrink(hotMachine, tea)
        UI.pushDrink(hotMachine, fruitTea)

    UI.showMachine(hotMachine)
    UI.saleHotDrink(hotMachine, "tea", 0.3, 50)
    print()
    UI.saleHotDrink(hotMachine, "tea", 0.3, 50)
    print()
    UI.saleHotDrink(hotMachine, "tea", 0.3, 50)
    print()
    UI.showMachine(hotMachine)
