# Day 4 Random Number Generate
# -->simple random number generate
# import random
# no_rand=random.randint(1,10)    #(starting,ending)
# print(no_rand)

# float random 0-5
# random.seed(55)
# float_random=random.random()
# print(round(float_random*5,2))

# Exercise Random coin task program
# test_seed=int(input('Create a seed Number \n'))
# random.seed(test_seed)
# rand=random.randint(0,1)
# if rand==1:
#     print('Heads')
# else:
#     print('Tails')


# List in python(Array)

# list_1=['apple',12,3.4,'hello']
# print(list_1[2])
# print(list_1[-1])
# list_1.extend(['o yeah',22])
# print(list_1)


# Exercise who's paying bill
# tst_seed=int(input('Create a seed Number'))
# random.seed(tst_seed)

# name_input=input('Enter names of your friend separated by comma :>')
# names=name_input.split(', ')
# index=len(names)
# a=random.randint(0,index-1)
# print(f'Name is {names[a]}')


# tressure map exercise
# row1=['❤️','❤️','❤️']
# row2=['❤️','❤️','❤️']
# row3=['❤️','❤️','❤️']

# map=[row1,row2,row3]
# print(f'{row1}\n{row2}\n{row3}')
# input1=input('Enter Number to place ')
# horizontal=int(input1[0])
# vertical=int(input1[1])

# select_row=map[vertical-1]
# select_row[horizontal-1]='⚠️'
# print(f'{row1}\n{row2}\n{row3}')


# print('''

          
#                             /   |
#                            |    |
#              _             |    |
#            /' |            | _  |
#           |   |            |    |
#           | _ |            |    |
#           |   |            |    |
#           |   |        __  | _  |
#           | _ |  __   /  \ |    |
#           |   | /  \ |    ||    |
#           |   ||    ||    ||    |       _---.
#           |   ||    ||    |. __ |     ./     |
#           | _. | -- || -- |    `|    /      //
#           |'   |    ||    |     |   /`     (/
#           |    |    ||    |     | ./       /
#           |    |.--.||.--.|  __ |/       .|
#           |  __|    ||    |-'            /
#           |-'   \__/  \__/             .|
#           |       _.-'                 /
#           |   _.-'      /             |
#           |            /             /
#           |           |             /
#           `           |            /
#            \          |          /'
#             |          `        /
#              \                .'
#              |                |
#              |                |
#              |                |
#              |                |

# ''')

