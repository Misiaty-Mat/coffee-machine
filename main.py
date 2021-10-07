# import data.py file with coffee informations and data
import data


# check if machine has enough resources to make specific coffee
def machine_resources_checker(total_resources, water_needed=0, milk_needed=0, coffee_needed=0):
    if total_resources["water"] < water_needed:
        print("Sorry not enough water")
        return False
    elif total_resources["milk"] < milk_needed:
        print("Sorry not enough milk")
        return False
    elif total_resources["coffee"] < coffee_needed:
        print("Sorry not enough coffee")
        return False
    else:
        return True

# payment management and give the change to user


def payment(cost):
    quarters = int(input('How many quarters would you like to put?: '))
    dimes = int(input('How many dimes would you like to put?: '))
    nickles = int(input('How many nickles would you like to put?: '))
    pennies = int(input('How many pennies would you like to put?: '))

    total_monney = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

    print(f"You entered {total_monney}$")

    if total_monney > cost:
        print("Coffee on the way!")
        change = round(total_monney - cost, 2)
        print(f"You paid {change}$ extra and it is your change")
        return True
    elif total_monney == cost:
        print("Coffee on the way!")
        return True
    else:
        money_needed = round(cost - total_monney, 2)
        print(f"You paid {money_needed}$ too little")
        print("Reseting order")
    return False


# importing dictionary with resources in the machine
resources = data.resources


while True:
    # user iteraction
    command = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    # turn off console
    if command == "off":
        break

    # make specific coffee
    elif command == "espresso":
        espresso_ingredients = data.MENU["espresso"]['ingredients']
        espresso_cost = data.MENU["espresso"]['cost']
        if machine_resources_checker(resources, espresso_ingredients["water"], coffee_needed=espresso_ingredients["coffee"]):
            print(f"It will be {espresso_cost}$")
            if payment(espresso_cost):
                resources["water"] -= espresso_ingredients["water"]
                resources["coffee"] -= espresso_ingredients["coffee"]
                resources["money"] += espresso_cost
    elif command == "latte":
        latte_ingredients = data.MENU["latte"]['ingredients']
        latte_cost = data.MENU["latte"]['cost']
        if machine_resources_checker(resources, latte_ingredients["water"], latte_ingredients["milk"], latte_ingredients["coffee"]):
            print(f"It will be {latte_cost}$")
            if payment(latte_cost):
                resources["water"] -= latte_ingredients["water"]
                resources["milk"] -= latte_ingredients["milk"]
                resources["coffee"] -= latte_ingredients["coffee"]
                resources["money"] += latte_cost
    elif command == "cappuccino":
        cappuccino_ingredients = data.MENU["cappuccino"]['ingredients']
        cappuccino_cost = data.MENU["cappuccino"]['cost']
        if machine_resources_checker(resources, cappuccino_ingredients["water"], cappuccino_ingredients["milk"], cappuccino_ingredients["coffee"]):
            print(f"It will be {cappuccino_cost}$")
            if payment(cappuccino_cost):
                resources["water"] -= cappuccino_ingredients["water"]
                resources["milk"] -= cappuccino_ingredients["milk"]
                resources["coffee"] -= cappuccino_ingredients["coffee"]
                resources["money"] += cappuccino_cost

    # report about resources that are left in the machine
    elif command == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {resources['money']}$")
    else:
        continue
