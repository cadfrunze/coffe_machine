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
banii_mei = 0
rest = 0
total_money = 0
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
def espresso():
    banii_mei = 0
    if MENU['espresso']['ingredients']['water'] <= resources['water'] and MENU['espresso']['ingredients']['coffee'] <= resources['coffee']:
        while banii_mei <= MENU['espresso']['cost'] or banii_mei > MENU['espresso']['cost']:
            print("This coffee cost : 1.5$")
            print(f"Remember:\nquarters: {quarters}$,\ndimes: {dimes}$,\nnickles: {nickles}$,\npennies: {pennies}$")
            print(f"Trebuie sa platesti: {round((MENU['espresso']['cost'] - banii_mei), 2)}")
            insert_coins = float(input("Insert coins: $"))
            banii_mei = banii_mei + round(insert_coins, 2)
            if banii_mei >= MENU['espresso']['cost']:
                resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
                print("Bucura-te de cafea!")
                return banii_mei
    else:
        print("Ne pare rau....nu mai avem resurse!")

while game:
    intrebare = input("What would you like? (espresso/latte/cappuccino):").lower()
    if intrebare == "off":
        print("Turn off the machine")
        game = False
    elif intrebare == "report":
        for a in resources:
            print(f"{a}: {resources[a]}")
    elif intrebare == "espresso":
        suma = espresso()
        rest = round((suma - MENU['espresso']['cost']), 2)
        banii_mei = banii_mei + rest
        suma = suma - rest
        total_money = total_money + suma
        resources['money'] = total_money
        if banii_mei > 0:
            print(f"Pana acum banii tai sunt: {banii_mei}")
            if rest > 0:
                print(f"Restul tau de la cafea este: {rest}")





