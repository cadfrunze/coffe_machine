from main import MENU, resources

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer

# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

# TODO 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

# TODO 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.

# TODO 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
game = True
money = 0
lista = []
monede = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

def alegere_cafea(intrebare):
    """Alegere cafea din meniu"""
    return MENU[intrebare]


def calc_meniu(cafeaua):
    """Calculator resurse"""
    for i in cafeaua['ingredients']:
        if cafeaua['ingredients'][i] > resources[i]:
            print("Ne pare rau...nu sunt destule resurse")
            return False

    else:
        return True




def monezi_cafea(money):
    """Introducere monezi pana la valoarea adevarata"""
    if meniu_calc == True:
        while money <= cafeaua['cost']:
            for a in monede:
                print(f"{a}: ${monede[a]}")
            print(f"Cafeaua ta {intrebare} costa {cafeaua['cost']}")
            for i in monede:
                cerere = int(input(f"How many {i}: "))
                money = money + (cerere * monede[i])
                if money >= cafeaua['cost']:
                    print(f"Ai introdus {money}....Cafeaua se prepara")
                    break
                else:
                    print(f"Pana acum ai introdus {money}")
            if money >= cafeaua['cost']:
                if money > cafeaua['cost']:
                    restul = money - cafeaua['cost']
                    money = money - restul
                    print(f"Poftim restul: {round(restul, 2)}")
                for i in cafeaua['ingredients']:
                    resources[i] = resources[i] - cafeaua['ingredients'][i]
                print(f"Enjoy the coffee {intrebare}")
                return money
            else:
                print("Ne pare rau....nu ai introdus destule monezi")
                return 0
    else:
        return 0


while game:
    intrebare = input("What would you like? (espresso/latte/cappuccino):").lower()
    if intrebare == "off":
        print("Turn off the machine")
        game = False
    elif intrebare == "report":
        for a in resources:
            if a == 'water' or a == 'milk':
                print(f"{a}: {resources[a]}ml")
            elif a == 'coffee':
                print(f"{a}: {resources[a]}g")
            elif a == 'money':
                print(f"{a}: ${resources[a]}")
    elif intrebare == "espresso" or intrebare == "latte" or intrebare == "cappuccino":
        cafeaua = alegere_cafea(intrebare)
        meniu_calc = calc_meniu(cafeaua)
        monezi = monezi_cafea(money)
        lista.append(monezi)
        if monezi > 0:
            resources['money'] = sum(lista)










