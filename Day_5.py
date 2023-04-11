# Day 5 Python Loops
# Simple for Loop
# items=['A','B','C','D']
# for i in items:
#     print(i)
#     print(items)

# Exercise to calculate student height
# 1st
# student_height=input('Enter Student Heights').split()
# for i in range(0,len(student_height)):
#     student_height[i]=int(student_height[i])
# print(int(sum(student_height)/len(student_height)))  
# 2nd 
# cal_height=0  
# student_height=input('Enter Student Heights').split()
# for i in range(0,len(student_height)):
#     student_height[i]=int(student_height[i])
#     cal_height=student_height[i]+cal_height
# average_height=cal_height/len(student_height)
# print(int(average_height))

# exercise to calculate highest score in class
# score_list=input('Enter Student Scores :>').split()
# max=0
# for i in range(0,len(score_list)):
#     score_list[i]=int(score_list[i])
#     if max<score_list[i]:
#         max=score_list[i]
# print(max)
# print(score_list)


# for loop range function
# add=0
# for number in range(1,101):
#  add=add+number
# print(add)

# for i in range(1,101,3):
#     print(i)

# exercise to add all eve number from 1-100
# add=0
# for i in range(1,101):
#     if i%2==0:
#         add=add+i
# print(add)

# job interview exercise
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print('fizzBuzz')
#     elif i%3==0:
#         print('Fizz')
#     elif i%5==0:
#         print('Buzz')
#     else:
#      print(i)    


#  Day 5 Final project 
# python password generator
# import random
# password=""
# letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
# 'o','p','q','r','s','t','u','v','w','x','v','z','A','B','C','D','E',
# 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
# 'W','X','Y','Z']
# numbers=['0','1','2','3','4','5','6','7','8','9']
# symbols=['!','@','#','$','%','&','(',')','+','*']
# print('Welcome to Python Password Generator')
# input_letters=int(input("How many letters you get in your password :"))
# input_numbers=int(input("How many numbers you get in your password :"))
# input_symbols=int(input("How many symbols you get in your password :"))
# for i in range(0,input_letters):
#     random_letter=random.choice(letters)
#     password=password+random_letter
# for i in range(0,input_numbers):
#     random_number=random.choice(numbers)
#     password=password+random_number
# for i in range(0,input_symbols):
#     random_symbols=random.choice(symbols)
#     password=password+random_symbols
    
# # print(f"Your Password is : {password}")