from random import choice
from coffee_machine_art import *

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def check_resources(order):
    for item in order:
        if order[item] >= resources[item]:
            print(f"Sorry there isn't enough {item}")
            return False
    return True


def funds():
    amount_quarters = float(input("How many quarters you want to insert? "))
    amount_dimes = float(input("How many dimes you want to insert? "))
    amount_nickles = float(input("How many nickels you want to insert? "))
    amount_pennies = float(input("How many pennies you want to insert? "))

    total_quarters = amount_quarters * 0.25
    total_dimes = amount_dimes * 0.10
    total_nickles = amount_nickles * 0.05
    total_pennies = amount_pennies * 0.01

    money = total_quarters + total_dimes + total_nickles + total_pennies
    return money


def make_coffee(drink_name, check_resources):
    for item in check_resources:
        resources[item] -= check_resources[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
            

is_on = True

while is_on:
    print(logo)
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            
            payment = funds()

            if payment > MENU[choice]["cost"]:
                profit += MENU[choice]["cost"]
                refund = payment - MENU[choice]["cost"]
                print(f"Here is ${round(refund,2)} in change.")
                make_coffee(choice, drink["ingredients"])

            else:
                print("Sorry that's not enough money. Money refunded.")



