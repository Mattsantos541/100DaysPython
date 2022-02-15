from coffee_menu_15 import MENU, resources

# TODO Prompt user by asking What would you like? (espresso/latte/cappuccino):
profit = 0

is_on = True

while is_on:
    choice = input("What wpould you like?  (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
# TODO Print report. a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
    if choice == "report":
