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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    if "money" in resources:
        print(f'Money: ${resources["money"]}')

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True
def process_coins():
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * .25
    total += int(input("how many dimes?: ")) * .10
    total += int(input("how many nickels?: ")) * .05
    return total

def is_transaction_successful(money_recieved, drink_cost):
    """return true when payment successful, return false if money is insufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"here is your change of {change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("That is not enough money.")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print("Here is your drink!")






