from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

process_on = True


my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while process_on:
    options = menu.get_items()
    choice = input(f"what would like to have {(options)}: ")
    if choice == "off".lower():
        process_on = False
    elif choice == "report".lower():
        coffee_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
