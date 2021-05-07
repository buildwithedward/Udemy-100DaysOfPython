from data import MENU, resources

machine_on = True

profit = 0


def is_resources_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there's no enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.1
    total += int(input("how many nickels: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, cost_drink):
    if money_received >= cost_drink:
        global profit
        profit += cost_drink
        print(f"Here is ${round(money_received - cost_drink,2)} in change")
        return True
    else:
        return "Sorry that's not enough money. Money Refunded"


def make_coffee(drink_selected, resources_default):
    for item in resources_default:
        resources[item] -= resources_default[item]
    print(f"Enjoy your {drink_selected}!!")


while machine_on:
    choice = input("what would you like (espresso/latte/cappuccino): ")
    if choice == "off".lower():
        machine_on = False
    elif choice == "report".lower():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "refill".lower():
        resources["water"] += abs(300 - resources["water"])
        resources["milk"] += abs(200 - resources["milk"])
        resources["coffee"] += abs(100 - resources["coffee"])
        print("Resources Refilled")

    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
