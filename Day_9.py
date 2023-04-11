# # Day 9 Python
# # Dictionary in python 
# # Syntax: name={key:Value}
# Alphabets={"a":"Apple",
#            "b":"Bat",
#            "c":"Cat"
# }
# # print(Alphabets["b"])
# # for adding new key in dictionary
# Alphabets["d"]="DOg"
# # print(Alphabets)
# # Alphabets={}
# # print(Alphabets)
# # Edit an item in dictionary 
# Alphabets["b"]="ball"
# # print(Alphabets)
# for letter in Alphabets :
#     print(letter)
#     print(Alphabets[letter])

# Coding Exercise to grades the student data
# Student_scores={
#     "Harry":81,
#     "Ron":78,
#     "Hermione":99,
#     "Draco":74,
#     "Neville":62,
    
# }
# Student_Grades={
    
# }
# for scores in Student_scores:
#     if Student_scores[scores]>90:
#         Student_Grades[scores]="Outstanding"
#     elif Student_scores[scores]>80:
#         Student_Grades[scores]="Expectation"
#     elif Student_scores[scores]>70:
#         Student_Grades[scores]="Acceptable"
#     elif Student_scores[scores]>60:
#         Student_Grades[scores]="Fail"
# for i in Student_Grades:
#     print(i)
#     print(Student_Grades[i])

# Nesting Dictionary
# Alphabets={"a":{"Apple","Allah"},
#             "b":"Bat",
#             "c":"Cat"
#  }

# nesting dictionary in list
# Alphabets=[{
#             "a":"Apple",
#             "b":"bat",
#             "Letters":26
# },{
#            "C":"cat",
#            "d":"Dog"
#    }             ]
# print(Alphabets[1])

# travel_log=[
#     {
#     "country":"France",
#     "visits":12,
#     "cities":["Paris","Lille","Dijon"]
        
#         },
#     {
#     "country":"Germany",
#     "visits":5,
#     "cities":["Berlin","Hamburg","Stuttgart"]   
#     }
#     ]
# def add_new_country(country,time,city_visits):
#     new_country={}
#     new_country["country"]=country
#     new_country["visits"]=time
#     new_country["cities"]=city_visits
#     travel_log.append(new_country)
# add_new_country("Russia",2,["Moscow","Saint Petersburg"])
# print(travel_log)

# Day 9 Project

# find highest bid in your friends
# import os
# check=False
# bid={}
# def highest_bid(bid_larger_check):
#     larger_bid=0
#     for i in bid_larger_check:
#         if bid_larger_check[i]>larger_bid:
#             larger_bid=bid_larger_check[i]
#             winner=i
#     print(f"the Winner name is {winner} and their bid is ${larger_bid}")        
# while not check:
#     name=input("Enter your Name: ")
#     bid_no=int(input("Enter Your Bid Amount $"))
#     check_1=input("Do you want to add more bid 'yes' or 'no'")
#     bid[name]=bid_no
#     if check_1=="yes":
#         os.system("cls")
#     elif check_1=="no":
#         check=True
#         highest_bid(bid)