# Budget App
# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories
#
# Push your code to GitHub, and submit the repo link.

categories = []


class Budget:
    def __init__(self, name, btc_balance):
        self.name = name
        self.btc_balance = btc_balance
        categories.append(self.name)

    def deposit(self, deposit_btc):
        self.btc_balance += deposit_btc
        return self.btc_balance

    def withdraw(self, withdraw_btc):
        self.btc_balance -= withdraw_btc
        return self.btc_balance

    def transfer(self, target, to_transfer):
        self.btc_balance -= to_transfer
        target.btc_balance += to_transfer
        return self.btc_balance

food_budget = Budget('food budget', 1000)
print(food_budget.name)
print(food_budget.btc_balance)
clothing_budget = Budget('clothing budget', 1000)
entertainment_budget = Budget('entertainment budget', 1500)
print(food_budget.withdraw(20))
food_budget.transfer(entertainment_budget, 20)
print(food_budget.name)
print(food_budget.btc_balance)
print(entertainment_budget.name)
print(entertainment_budget.btc_balance)
entertainment_budget.transfer(clothing_budget, 300)
print(entertainment_budget.name)
print(entertainment_budget.btc_balance)
print(clothing_budget.name)
print(clothing_budget.btc_balance)
print(food_budget.withdraw(200))
print(food_budget.deposit(500))
print(categories)