# day 11 blackjack Game


# function for get random cards
# import random
# import os
# def display():
#     print('''
                                                                                             
# 88          88                       88        88                       88         
# 88          88                       88        ""                       88         
# 88          88                       88                                 88         
# 88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
# 88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
# 88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
# 88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
# 8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
#                                               ,88                                  
#                                             888P"                                  

#           ''')
# def deal_card():
#     cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
#     card=random.choice(cards)
#     return card
# game_control=False
# inner_check=False
# # //calculate sum of cards
# def calculate_score(cards):
#     if sum(cards)==21 and len(cards)==2:
#         return 0
#     if 11 in cards and sum(cards)>21:
#         cards.remove(11)
#         cards.append(1)
#         return sum(cards)
#     return sum(cards)    
# user_card=[]
# computer_card=[]
# display()
# in1=input("Do you want to play game of Blackjack type y or n: ")
# if in1=="y":
#     while not game_control:
#         for i in range(2):
#             user_card.append(deal_card())
#             computer_card.append(deal_card())
#         user_sum=calculate_score(user_card)
#         computer_sum=calculate_score(computer_card)
#         if user_sum==0:
#             print(f"User Card: {user_card} ,Current Score:21")
#             print(f"Computer Card: {computer_card} ,Current Score: {computer_sum}")
#             inner_check=True
#         elif computer_sum==0:
#             print(f"user Card: {user_card} , current score: {user_sum}")
#             print(f"Computer Card: {computer_card} ,Current Score:21")
#             inner_check=True
#         elif user_sum>21:
#             print(f"user Card: {user_card} , current score: {user_sum}")
#             print(f"Computer Card: {computer_card} ,Current Score: {computer_sum}")
#             inner_check=True
#         #    print(f"Your Cards: {user_card} , Current Score {user_sum}")
#         #    print(f"Computer Cards: {computer_card} , Current Score {computer_sum}")
#         #    break
#         else:
#             print(f"Your Cards: {user_card} , Current Score {user_sum}")
#             print(f"Computer's First Card: {computer_card[0]}")
        
#             while not inner_check:
#                 in2=input("Type y to get another card , type n to pass: ")
#                 if in2=="y":
#                     another_card=deal_card()
#                     user_card.append(another_card)
#                     another_sum=calculate_score(user_card)
#                     user_sum=another_sum
#                     if another_sum==0 or another_sum>21:
#                         print(f"Your Cards: {user_card} , Current Score {another_sum}")
#                         print(f"Computer Cards: {computer_card} , Current Score {computer_sum}")
#                         inner_check=True
#                         break
#                     else:
#                         print(f"Your Cards: {user_card} ,current Score: {another_sum}")
#                         print(f"Computer's First Card: {computer_card[0]}")
#                 elif in2=="n":
#                     inner_check=True
#                     loo=False
#                     while not loo:
#                         if computer_sum<16:
#                             another_card=deal_card()
#                             computer_card.append(another_card)
#                             another_sum_c=calculate_score(computer_card)
#                             computer_sum=another_sum_c
#                             if another_sum_c==0 or another_sum_c>21:
#                                 print(f"Your Cards: {user_card} , Current Score {user_sum}")
#                                 print(f"Computer Cards: {computer_card} , Current Score {computer_sum}")
#                                 loo=True
#                                 break
#                             else:
#                                 print(f"Computer Cards: {computer_card} , current score: {another_sum_c}")
                        
#                         else:
#                             print(f"Computer Cards: {computer_card} , current score: {computer_sum}")
#                             loo=True                 
#         if user_sum>computer_sum and user_sum>21:
#             print("You Lose!")   
#         elif computer_sum>user_sum and computer_sum<=21:
#             print("You Lose!")
#         elif user_sum>computer_sum and user_sum<=21:
#             print("You Win!")
#         elif computer_sum==user_sum:
#             print("Match Draw")
#         in3=input("Do you want to play game of Blackjack type y or n: ")
#         user_card.clear()
#         computer_card.clear()
#         inner_check=False
#         os.system("cls")
#         display()
#         if in3=="n":
#             game_control=True 
