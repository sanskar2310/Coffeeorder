MENU = {
    "espresso": {
        "ingredients": {
            "water": 150,
            "coffee": 36},
        "cost": 50,
    },
    "latte": {
        "ingredients": {
            "water": 300,
            "coffee": 48,
            "milk": 250},
        "cost": 40,
    },
    "cappuccino": {
        "ingredients": {
            "water": 400,
            "coffee": 40,
            "milk": 150},
        "cost": 70,
    }
}
profit = 0
resource = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
}


def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print(f"Sorry, {item} is not enough for your order!")
            is_enough = False
    return is_enough


def process_coin():
    print("Please insert coins.")
    total = int(input("How many 20Rs coin?: ")) * 20
    total += int(input("How many 10Rs coin?: ")) * 10
    total += int(input("How many 5Rs coin?: ")) * 5
    total += int(input("How many 2Rs coin?: ")) * 2
    total += int(input("How many 1Rs coin?: ")) * 1
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is Rs{change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. ENJOY!")


is_on = True
while is_on:
    choice = input("What would you like to have? (espresso Rs50/latte Rs40/cappuccino Rs70): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: Rs{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
