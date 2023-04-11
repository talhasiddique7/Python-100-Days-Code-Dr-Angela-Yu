# # Day 7
# # Hangman game
# # step 1
# import random
# import os
# print(''' 
# __                                                 
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/     ''')

# hangman=[''' 
#             +__+
#             |  |
#             O  |
#            /|\ | 
#            / \ |
#                |
#                |
#     ___________
#     ___________           
     
#  ''',
#  ''' 
#             +__+
#             |  |
#             O  |
#            /|\ | 
#            /   |
#                |
#                |
#     ___________
#     ___________           
     
#  ''',
#  ''' 
#             +__+
#             |  |
#             O  |
#            /|\ | 
#                |
#                |
#                |
#     ___________
#     ___________           
     
#  ''',
#  ''' 
#             +__+
#             |  |
#             O  |
#            /|  | 
#                |
#                |
#                |
#     ___________
#     ___________           
     
#  ''',
#  ''' 
#             +__+
#             |  |
#             O  |
#             |  | 
#                |
#                |
#                |
#     ___________
#     ___________           
     
#  ''',
#  ''' 
#             +__+
#             |  |
#             O  |
#                | 
#                |
#                |
#                |
#     ___________
#     ___________           
     
#  ''',
#  ''' 
#             +__+
#             |  |
#                |
#                | 
#                |
#                |
#                |
#     ___________
#     ___________           
     
#  ''']
# display=[]
# lives=7
# list_names=["ali","talha","lakhte","ramish","muneeb"]
# select_random=random.choice(list_names)
# for i in range(len(select_random)):
#     display+="_"
#     print(display[i]+" ")
# # print(select_random)
# check1=False
# check_blank=False
# while not check_blank:
#     input_user=input("Guess a letter ").lower()
#     for check in range(len(select_random)):
#         letter=select_random[check]
#         if letter==input_user:
#             display[check]=letter
#             check1=True
#         if '_' not in display:
#             check_blank=True
#             print(display)
#             print("You Win!")
#             break
#     if check1==False:
#         lives=lives-1
#         os.system("cls")
#         print(hangman[lives])
#         if lives==0:
#             print("You Lose!")
#             check_blank=True
#             break 
#     check1=False       
#     print(display)

        
