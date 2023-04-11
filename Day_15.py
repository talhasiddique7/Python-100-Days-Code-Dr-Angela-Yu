# # day 15 Project: Coffee Machine
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# Money = 0
# check = False
# Penny = 0.01
# Dime = 0.10
# Nickel = 0.05
# Quarter = 0.25
# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("Sr#",["1","2","3"])
# table.add_column("Coffee",["espresso","latte","cappuccino"])
# table.add_column("Price",["$1.5","$2.5","$3.5"])
# print(table)
# # for check coffee ingredients to resources
# def is_resources_sufficient(order):
#     for item in order:
#         if order[item] >= resources[item]:
#             print(f"Sorry there is not enough {item}")
#             return False
#     return True

# # Money convert in dollars


# def money_converter():
#     print("Please insert coin.")
#     total = int(input("How Many Quarters?: "))*0.25
#     total += int(input("How Many Dimes?: "))*0.10
#     total += int(input("How Many nickles?: "))*0.05
#     total += int(input("How Many Pennies?: "))*0.01
#     return total

# # Check user coin to coffee price and return result


# def transaction_details(payment, cost):
#     if payment < cost:
#         print(f"Sorry you have insufficient Balance.Money Refunded.")
#         return False
#     else:
#         change = round(payment-cost, 2)
#         print(f"Your Change : ${change}")
#         global Money
#         Money += payment
#         Money = round(Money, 2)
#         return True

# # for manage materials(Coffee)


# def manage_material(material):
#     for item in material:
#         resources[item] -= material[item]


# while not check:
#     input1 = input("What would you like?(espresso/latte/cappuccino): ")
#     if input1 == "off":
#         check = True
#     elif input1 == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${Money}")
#     else:
#         drink = MENU[input1]
#         if is_resources_sufficient(drink["ingredients"]):
#             bill = money_converter()
#             if transaction_details(bill, drink["cost"]):
#                 manage_material(drink["ingredients"])
#                 print(f"Enjoy Your Coffee: {input1}")
