from data import resources
from data import MENU


# 1: Display report to the Operator at the start of the day
print(resources)


water = resources['water']
milk = resources['milk']
coffee = resources['coffee']

check = True

while check:
    # 2: Ask user to input the coffee type which like to have
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off".lower():
        check = False

    else:

        # 3: As soon user inputs the type, check the resources are available or not
        # 3.1: Extract the details of user's coffee resources and compare with overall resources
        user_choice = MENU[choice]["ingredients"]

        user_water = user_choice["water"]
        user_coffee = user_choice["coffee"]
        try:
            user_milk = user_choice["milk"]
        except:
            user_milk = 0
        money = MENU[choice]["cost"]

        if water >= user_water:
            print("Please insert coins.")
            quarters = float(input("how many quarters: ")) * 0.25
            dimes = float(input("how many dimes: ")) * 0.10
            nickels = float(input("how many nickels: ")) * 0.05
            pennies = float(input("how many pennies: ")) * 0.01

            total = quarters + dimes + nickels + pennies

            if total > money:
                print(f"Here is {round(total - money, 2)} in change")
                print(f"Here is your {choice} enjoy!")
                water = water - user_water
                milk = milk - user_milk
                coffee = coffee - user_coffee
            else:
                print(f"Not enough money, {money} is refunded")
        else:
            print("sorry there is not enough water")

# 4: If resources aren't available, show sorry there is not enough water. Ask operator to refill
# 4: If resources are available, ask user to put coins

        # 5:Calculate the sum of coins and check whether user can buy coffee
        # 5.1 if yes, calculate the excess money, give the change and greet user to enjoy coffee
        # 5.1.1 Simultaneously update the resources after deducting previous coffee resources
        # 5.2 if no, show user the money has refunded

        # 6. Repeat the steps from 2 until someone enters 'Off' and stops the coffee machine
