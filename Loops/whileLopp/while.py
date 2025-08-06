# a=1
# while a<=30:
#     a=a+1
    
#     print(a)

# questions with answers for whileloop

# Separate each digit of a number and print it on the new line
# a = int(input("Tell your number: "))
# while a > 0:
#     print(a % 10)  # Print last digit
#     a = a // 10    # Remove last digit

# Accept a number and print its reverse
# a = int(input("Tell your number: "))
# rev=0

# while a > 0:
#     rev=rev * 10 + a % 10
   
#     a = a // 10 
#     print(rev) 

    #  Accept a number and check if it is a pallindromic number (If
# number and its reverse are equal?  
# a = int(input("Tell your number: "))
# rev = 0
# copy = a

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# if copy == rev:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")
# guess ab number and play game
import random
num=random.randint(1,10)
tries=0
while True:
    guess=int(input("please guess your number between 1 and 10 :- "))
    if num==guess:
        tries+=1
        print(f"you are right you guesses the {tries} tries ")
        break
    elif num < guess :
        print("go a little lower")
        tries +=1
    elif num > guess :
        print("go to a heigher lower")
        tries +=1
    else:
        print("you are wrong")

