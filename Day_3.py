# Day 3 Conditional Statement 

# if-else 
# -->Day 3.1 Exercise check wether the number is even or ood
# check_number=input('Enter Check Number ?')
# check_number=int(check_number)
# if check_number%2==0:
#     print('Even Number')
# else:
#     print('Odd Number')

# -->nested if-else statement 
# print('Welcome to the Rollercoaster!')
# height=int(input('Enter your Height:'))

# if height>120:
#     age=int(input('Enter your Age:'))
#     print('You Can Ride Rollercoaster')
#     if age>18:
#         print('and you pay $12')
#     elif age<12:
#         print('and you pay $5') 
#     else:
#         print('and you pay $7')     
# else:
#       print('Sorry,You cannot ride Rollercoaster')  


    
#    BMI 2.0 using conditional statement
# height=float(input('Enter your Height(m) ? \n'))
# weight=float(input('Enter your Weight (Kg)? \n'))
# bmi=(weight)/(height)**2
# bmi=round(bmi)
# if bmi<=18.5:
#     print(f'Your bmi is {bmi},You are under weight')
# elif bmi<25:
#     print(f'Your bmi is {bmi},You are normal weight')
# elif bmi<30:
#     print(f'Your bmi is {bmi},You are over weight')
# elif bmi<35:
#     print(f'Your bmi is {bmi},You are obese')
# else:
#     print(f'Your bmi is {bmi},You are clinically obese')            


# exercise to check leap year

# leap_year=int(input('Enter Year'))
# if leap_year%4==0:
#     print(f'{leap_year} is Leap Year')
# else:
#     print(f'{leap_year} not Leap Year')    


#Python Exercise Pizza delivery

# print('Welcome to Python Pizza Shop :)\n')
# print('Rate List ')
# print('Small Pizza $15')
# print('Medium Pizza $20')
# print('Large Pizza $25')
# print('Pepperoni for Small Pizza = +$2')
# print('Pepperoni for Medium or Large Pizza = +$3')
# print('For Extra Cheese = +$1\n')
# pizza_size=str(input('Enter Pizza Size Which You Want to buy? 'S','M' or 'L' :>'))
# pepperoni=str(input('Do you Want to Add Pepperoni?'Y' or 'N' ;:>'))
# cheese=str(input('Do you Want to Add extra cheese?'Y' or 'N' :>'))
# if (pizza_size=='S'):
#     pizza_size='15'
#     if pepperoni=='Y':
#         pepperoni='2'
#     if cheese=='Y':
#         cheese='1'    
# elif pizza_size=='M':
#     pizza_size='20'
#     if pepperoni=='Y':
#         pepperoni='3'
#     if cheese=='Y':
#         cheese='1'    
# elif pizza_size=='L':
#     pizza_size='25'
#     if pepperoni=='Y':
#         pepperoni='3'
#     if cheese=='Y':
#         cheese='1'
# if pepperoni=='N':
#     pepperoni='0'
# if cheese=='N':
#     cheese='0'            
# total=int(pizza_size)+int(pepperoni)+int(cheese)
# print(f'Your Bill is :${total}')


# Next exercise love calculator
# print('Welcome to Love Calculator :)')
# name1=input('Enter Your Name :')
# name2=input('Enter Your Partner Name :')
# plus_str=name1+name2
# plus_str=plus_str.lower()
# t=plus_str.count('t')
# r=plus_str.count('r')
# u=plus_str.count('u')
# e=plus_str.count('e')
# count1=t+r+u+e
# l=plus_str.count('l')
# o=plus_str.count('o')
# v=plus_str.count('v')
# e=plus_str.count('e')
# count2=l+o+v+e
# print('Your Score is :'+str(count1)+str(count2))


# Day 3 Project

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=''_;=.______________|_____________________|_______
# |                   |  ,-'_,=''     `'=.|                  |
# |___________________|__'=._o`'-._        `'=.______________|___________________
#           |                `'=._o`'=._      _`'=._                     |
#  _________|_____________________:=._o '=._.'_.-='''=.__________________|_______
# |                   |    __.--' , ; `'=._o.' ,-'''-._ '.   |
# |___________________|_._'  ,. .` ` `` ,  `'-._'-._   '. '__|___________________
#           |           |o`'=._` , '` `; .'. ,  '-._'-._; ;              |
#  _________|___________| ;`-.o`'=._; .' ` '`.'\` . '-._ /_______________|_______
# |                   | |o;    `'-.o`'=._``  '` ' ,__.--o;   |
# |___________________|_| ;     (#) `-.o `'=.`_.--'_o.-; ;___|___________________
# ____/______/______/___|o;._    '      `'.o|o_.--'    ;o;____/______/______/____
# /______/______/______/_'=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__'=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____'=._o._; | ;_.--'o.--'_/______/______/______/_
# ____/______/______/______/______/_____'=.o|o_.--''___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_______/
# *******************************************************************************
# ''')
# print('Welcome to treasure Island')
# print('Your Mission is to find the Treasure')
# in1=(input('You're at a cross road.Where do you want to go?Type 'left' or 'right'  '))
# if in1=='right':
#     print('Game Over')
# elif in1=='left':
#     in2=input('You came to a lake.There is an island middle of the lake. Type 'wait' to wait for a boat. type 'swim' to swim across  ') 
# if in2=='swim':
#  print('Game Over')
# elif in2=='wait':
#     in3=input('You arrive at the island unharmed. There is a house with 3 doors. One red,one yellow and one blue.Which color do you choose?  ')
#     if in3=='blue':
#         print('Game Over')
#     elif in3=='red':
#         print('Game Over')
#     else:
#         print('You Win!')            