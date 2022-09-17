from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    order = input(f"What would you like? {options}:")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        resource = coffee_maker.is_resource_sufficient(drink)
        if not resource:
            print(resource)
            continue
        else:
            money = money_machine.make_payment(drink.cost)
            if money:
                coffee_maker.make_coffee(drink)
