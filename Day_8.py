# Day 8 Function with argument and parameters
# greet()
# def greet():
#     print("The president rose to greet his guests.")
#     print("The two men greeted one another warmly.")
#     print("You must be there to greet your guests.")
# greet()

# greet() with parameter
# def greet(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
# inp=input("Enter Name :")
# greet(inp)

# Prime Number Check

# def prime(prime_number):
#     is_prime=True
#     if prime_number==0 or prime_number==1:
#         print("Not a Prime Number")
#         return
#     check=prime_number/2
#     check=int(check)
#     i=2
#     for i in range(2,check):
#         if prime_number%i==0:
#             print("Not a prime Number")
#             is_prime=False
#             break
        
#     if is_prime==True:
#         print("Prime Number")   
# prime(9)

# Final Day 8 project

# print('''
                                                                                                                   
                                                                                                             
#     //   ) )                                                  //   ) )                                       
#    //         ___      ___      ___      ___      __         //        ( )  ___     / __      ___      __    
#   //        //   ) ) //___) ) ((   ) ) //   ) ) //  ) )     //        / / //   ) ) //   ) ) //___) ) //  ) ) 
#  //        //   / / //         \ \    //   / / //          //        / / //___/ / //   / / //       //       
# ((____/ / ((___( ( ((____   //   ) ) ((___( ( //          ((____/ / / / //       //   / / ((____   //     ''')
# check=True
# letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','v','z',
#          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','v','z']

# def encrypt(plain_text,shift):
#     encrypt1=""
#     for letter in plain_text:
#         i=letters.index(letter)
#         i=i+shift
#         encrypt1+=letters[i]
#     print(f"The encoded message is : {encrypt1})
# def decrypt(plain_text,shift):
#     decrypt1=""
#     for letter in plain_text:
#         i=letters.index(letter)
#         i=i-shift
#         decrypt1+=letters[i]
#     print(f"The Decoded Message is : {decrypt1})
# while(check==True):
#     check_method=input("\n\nType 'encode' to encrypt, type 'decode' to decrypt\n")
#     if(check_method=="encode"):
#         n_in=input("Type Your Message :\n").lower()
#         n_num=int(input("Type the shift Number \n"))
#         encrypt(n_in,n_num)
#     if(check_method=="decode"):
#         n_in=input("Type Your Message :\n").lower()
#         n_num=int(input("Type the shift Number \n"))
#         decrypt(n_in,n_num)
#     terminate=input("Type 'yes' if you want to again,otherwise type 'no'\n").lower()
#     if terminate=="no":
#         check=False
