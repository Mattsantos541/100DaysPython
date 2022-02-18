from coffee_menu_15 import MENU, resources, print_report, is_resources_sufficient, \
    process_coins, is_transaction_successful, make_coffee

# TODO Prompt user by asking What would you like? (espresso/latte/cappuccino):
profit = 0

is_on = True

while is_on:
    choice = input("What would you like?  (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
# TODO Print report. a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
    elif choice == "report":
        print_report()
    else:
        drink = MENU[choice]
        print(drink)
        is_resources_sufficient(drink["ingredients"])
        payment = process_coins()
        if is_transaction_successful(payment, drink["cost"]):
            make_coffee(choice, drink["ingredients"])

