#Data Types

#String 
# -->  such as 'Hello world'

#Integer --> 1234

#float   -->1.24

#Bool     --> true or false

# int_value=len(input('What is your name ?'))
# string_value=str(int_value)
# print('Your name has ' + string_value + ' characters')

# print(type(int_value))
# print(type(string_value))

# Data type exercise
# -->enter two digit number the program output sum of 
# two number such as user input 23 the program output answer
# is 5 ?
# two_number=input('Enter two number value ?')
# first=two_number[0]
# second=two_number[1]
# result=int(first)+int(second)
# print(result) 


# Exercise to calculate Body mass index (BMI) ?
# formula = weight/height**2

# height=input('Enter your Height(m) ? \n')
# weight=input('Enter your Weight (Kg)? \n')
# bmi=int(weight)/float(height)**2
# bmi=int(bmi)
# print('Your Body mass index is ' + str(bmi))

#Round() -->for round of value
# print(round(8/3))
#print(round(8/3,4))
# print(8/3)
# print(8//3)
#f-string type
# integer=124
# float1=12.4
# bool1=True

# print(f'integer value {integer}, float value {float1} boolean value {bool1},')


#Exercise to get age from user and print
# days weeks and months of your age?

# age=input('Enter your Age \n')
# age=int(age)
# days=((90-age)*365)
# weeks=((90-age)*int(365/7))
# months=((90-age)*12)
# print(f'Your have  Months {months},Weeks {weeks} and Days {days} left')


#Day 2 Project 
# -->tip calculator ?

# print('Welcome to Tip Calculator \n')
# bill=input('What was th total bill?  $ ')
# tip=input('What percentage tip would you like to give? 10, 12 or 15 :>')
# people=input('How many people to split the bill? ')
# bill=float(bill)
# bill=bill+((bill*int(tip))/100)
# bill=bill/int(people)
# bill=round(bill,2)
# print('Each person should pay : $'+str(bill))
