# Day 10 Function and build a Calculator
# return functions
# def call_function():
#     return(3+7)
# output=call_function()
# print(output)

# Coding exercise to find the days in month
# import os
# days=[31,28,31,30,31,30,31,31,30,31,30,31]
# def days_in_month(Year,month_number):
#     if Year%4==0:
#         if month==2:
#             return(days[month_number-1]+1)
#     else:
#         return(days[month_number-1])
# check=False
# while not check:
#     Year=int(input("Enter year :"))
#     month=int(input("Enter Month Number :"))
#     answer=days_in_month(Year,month)
#     print(answer)
#     check_input=input("Do you want to check again yes or no ")
#     if check_input=="yes":
#         os.system("cls")
#     else:
#         check=True
# final day project to make calculator

# import os
# def add_function(i1,i2):
#     return(i1+i2)
# def sub_function(i1,i2):
#     return(i1-i2)
# def mul_function(i1,i2):
#     return(i1*i2)
# def div_function(i1,i2):
#     return(i1/i2)
# def display():
#  print('''
                                                                             
#            _            __      __        
#           | |          | |     | |            
#   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
#  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
# | (_| (_| | | (__| |_| | | (_| | || (_) | |   
#  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                     
#  _____________________
# |  _________________  |
# | |              0. | |
# | |_________________| |    
# |  ___ ___ ___   ___  |
# | | 7 | 8 | 9 | | + | |
# | |___|___|___| |___| |
# | | 4 | 5 | 6 | | - | |
# | |___|___|___| |___| |
# | | 1 | 2 | 3 | | x | |
# | |___|___|___| |___| |
# | | . | 0 | = | | / | |
# | |___|___|___| |___| |
# |_____________________|
#       ''')
# display()
# check=False
# while not check:
#     in1=int(input("Enter First Number : "))
#     input1=input("Choose One Operator \n+\n-\nx\n/\n-->")    
#     in2=int(input("Enter Second Number : "))
#     if input1=="+":
#         result=add_function(in1,in2)
#         print(f"{in1} {input1} {in2} = {result}")
#     elif input1=="-":
#         result=sub_function(in1,in2)
#         print(f"{in1} {input1} {in2} = {result}")
#     elif input1=="x":
#         result=mul_function(in1,in2)
#         print(f"{in1} {input1} {in2} = {result}")
#     elif input1=="/":
#         result=div_function(in1,in2)
#         print(f"{in1} {input1} {in2} = {result}")
#     check_for=input("type y for more calculation and n for exit ")
#     if check_for=="n":
#         check=True