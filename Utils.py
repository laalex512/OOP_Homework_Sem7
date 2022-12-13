from HotDrink import *
from Drink import *
from HotDrinkMachine import *
from VendingMachine import *


class Utils:

    def showMachine(vendingMachine):
        vendingMachine.viewMachine()

    def pushDrink(vendingMachine, drink):
        vendingMachine.pushDrink(drink)
        
    def saleAllDrink(vendingMachine,drink):
        vendingMachine.saleDrink(drink)
        
    def saleHotDrink(hotMachine, name, volume, temperature):
        hotMachine.saleDrink(name, volume, temperature)
