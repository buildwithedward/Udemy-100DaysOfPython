from resources import money, cards
import random


ATM_money = 0


def atm_sufficient(default):
    global ATM_money
    for item in default:
        ATM_money += item * default[item]
    if ATM_money < 500:
        return False
    return True


def pass_check(card_selected):
    pin_number = int(input("Enter your four digit PIN number: "))
    card_pin = cards[card_selected]["password"]
    if card_pin == pin_number:
        return True
    return "Password incorrect"


def bank_operation(user_choice, card_selected):
    global ATM_money, transaction_on
    if pass_check(card_selected):
        if user_choice == "statement":
            print(
                f"Your available balance is {cards[card_selected]['balance']}")
            transaction_on = False

        elif user_choice == "withdrawal".lower():
            amount = int(input("Enter amount to be withdrawn/deposit: "))
            if amount < cards[card_selected]["balance"]:
                cards[card_selected]["balance"] -= amount
                ATM_money -= amount
                print("Take your money and card. ATM won't take back your money")
            else:
                print("your account doesn't have sufficient balance")
                transaction_on = False

        elif user_choice == "deposit".lower():
            amount = int(input("Enter amount to be withdrawn/deposit: "))
            cards[card_selected]["balance"] += amount
            ATM_money += amount
            print("Amount Deposited! Have a nice day! ")


def proceed_transaction():
    global transaction_on
    proceed = input("Do you want to continue transaction? y/n: ").lower()
    if proceed == 'y':
        transaction_on = True
    elif proceed == 'n':
        transaction_on = False
        print("Thank you for banking with us. Have a nice day!")
    else:
        print("Wrong Entry")
        transaction_on = False


transaction_on = True
card_display = random.choice(list(cards.keys()))
print(card_display)
print(cards[card_display]["password"])
print(f"Welcome {cards[card_display]['name']}")

while transaction_on:
    if atm_sufficient(money):
        choice = input("what would you like to do (withdrawal/deposit): ")
        bank_operation(choice, card_display)
        proceed_transaction()
    else:
        print("Out of Cash. Please check our nearby ATM")
