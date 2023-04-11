# Day 12 scope

# enemies=1
# def change():
#     enemies=2
#     print(f"enemies value {enemies}")
# change()
# print(f"enemies value {enemies}")

# Local Scope
# in local scope inside variable create not accessible for outside
# def variable():
#     value=3
#     print(value)
# variable()
# print(value)  error

# Global Scope
# enemies=1
# def change():
#     print(f"enemies value {enemies}")
# change()


# In python their is no global scope
# such as 
# if 3>3:
#     new=3
# else:
#     new=4
# print(new)



# enemies=1
# def change():
#     global enemies #define global variable inside the function
#     enemies=2
#     print(f"enemies value {enemies}")
# change()
# print(f"enemies value {enemies}")

# Global scope use when you use constant value in your code


# Final Day Project number Guessing
# Global Variable
# import random
# r_generate=random.randint(1,100)
# easy_level=10
# hard_level=5
# e_level=10
# h_level=5
# print('''
#     //   ) )                                       /__  ___/                     /|    / /                                              
#    //                  ___      ___      ___         / /  / __      ___         //|   / /           _   __     / __      ___      __    
#   //  ____  //   / / //___) ) ((   ) ) ((   ) )     / /  //   ) ) //___) )     // |  / / //   / / // ) )  ) ) //   ) ) //___) ) //  ) ) 
#  //    / / //   / / //         \ \      \ \        / /  //   / / //           //  | / / //   / / // / /  / / //   / / //       //       
# ((____/ / ((___( ( ((____   //   ) ) //   ) )     / /  //   / / ((____       //   |/ / ((___( ( // / /  / / ((___/ / ((____   //  
#       ''')
# print(r_generate)
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# inp1=input("Choose a difficulty.Type 'easy' or 'hard': ")
# if inp1=="easy":
#     while easy_level>=1:
#         print(f"Y0u Have {easy_level} attempts to guess a number.")
#         ch_easy=int(input("Make a Guess: "))
#         if ch_easy==r_generate:
#             print("You Win!")
#             easy_level=0
#         elif ch_easy>r_generate:
#             print("too high.")
#             easy_level-=1
#             e_level-=1
#         elif ch_easy<r_generate:
#             print("Too Low.")
#             easy_level-=1
#             e_level-=1
#     if easy_level==0:
#         print("You Lose!")
# elif inp1=="hard":
#     while hard_level>=1:
#         print(f"You Have {hard_level} attempts to guess a number.")
#         ch_hard=int(input("Make a Guess: "))
#         if ch_hard==r_generate:
#             print("You Win!")
#             hard_level=0
#         elif ch_hard>r_generate:
#             print("too high.")
#             hard_level-=1
#             h_level-=1
#         elif ch_hard<r_generate:
#             print("Too Low.")
#             hard_level-=1
#             h_level-=1
#     if h_level==0:
#         print("You Lose!")