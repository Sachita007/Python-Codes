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



def resource_check(water, milk, coffee, order):
    """This function return True if resource is sufficient else it will return insufficient resource"""
    if order == "espresso":
        if water < MENU[order]['ingredients']['water']:
            return "water"
        elif coffee < MENU[order]['ingredients']['coffee']:
            return "coffee"
        else:
            return True
    elif order == "latte" or order == "cappuccino":
        if water < MENU[order]['ingredients']['water']:
            return "water"
        elif coffee < MENU[order]['ingredients']['coffee']:
            return "coffee"
        elif milk < MENU[order]['ingredients']['milk']:
            return "milk"
        else:
            return True


def money_check(quarters, dimes, nickles, pennies, order):
    """This function check and return left of money else if money is in sufficient it's return False"""
    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    if total > MENU[order]['cost']:
        left = total - MENU[order]['cost']
        return "%.2f" % left
    else:
        return False


# Initial Resources
water = 300
milk = 200
coffee = 100
money = 0
should_continue = True

while should_continue:
    # TODO: Asking user order coffee
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "report":
        print(f"Water = {water}ml")
        print(f"Milk = {milk}ml")
        print(f"Coffee = {coffee}gm")
        print(f"Money = ${money}")
        continue
    elif order == "off":
        should_continue = False
    resource = resource_check(water, milk, coffee, order)
    if resource:
        # TODO: Asking for coins for ordering coffee
        quarters = int(input("how many quarters?:"))
        dimes = int(input("how many dimes?:"))
        nickles = int(input("how many nickles?:"))
        pennies = int(input("how many pennies?:"))

        # TODO: Checking money is sufficient for order or not
        bill = money_check(quarters, dimes, nickles, pennies, order)
        if not bill:
            print("Sorry that's not enough money.Money Refunded.")
        else:
            print(f"Here is ${bill} in change.")
            print(f"Here is your {order}. Enjoy!")
            money = money + MENU[order]['cost']
            if order == "latte" or order == "cappuccino":
                milk = milk - MENU[order]['ingredients']['milk']
            coffee = coffee - MENU[order]['ingredients']['coffee']
            water = water - MENU[order]['ingredients']['water']
