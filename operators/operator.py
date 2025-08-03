# aitrhmetics opertaor
#  += Add and assigD
#  -= Subtract and assigD
#  *= Multiply and assignA
#  /= Divide and assigD
#  //= Floor divide and assigD
#  %= modulus and assigD
#  **= Exponentiation and assign

a=32
b=15
print(a+b)
print(b-a)
print(a*b)
print(a/b)
print(a//b)
print(a**b)


# 5 Comparison operators, also called relational operators, are
# used to compare two values
# 5 Comparison operators will always provide Boolean result that
# is True and False
# 5 comparison operators are as follow
# 5 == Equal t<
# 5 != Not Equal to3
# 5 > Greater than3
# 5 < Less than 3
# 5 >= Greater than or equal t<
# 5 <= Less than or equal t<
# 5 Comparison operators will work with numbers but you can
# use them with strings as well.3
# 5 Strings will be comparing the Ascii values of string.
# 5 Logical operators in Python are used to combine multiple
# conditions and return a Boolean result (True or False)
# 5 There are 3 types of logical operator3
# 5 and - Return True if both condition are Tru\
# 5 or - Return True if at least one condition is True
# a=20
# a+=40
# a+=60
# a+=80

# print(a)

c=13
d=56
print(c==d)
print(c!=d)

print(c>d)
print(d<c)
print(23<=23)
print(20<=12)
print (ord("A"))

# logical operators
# and or not are logical operators
print(80<=25 and 23>=23) 
print(20>10 and 30<45 and 67<80)
print(20>10 or  30<45 or 67<=80)
print (20!=40 and 40==40)

# conditional operators
# if else statement

a = 10
if a > 12:
    print("I am greater than 12")
else:
    print("I am less than 12")



    # money=int(input("please provide me the money:--"))
    
    # if money < 10:
    #     print("i am eating the icecream")
    # elif money > 20:
    #     print("iam eating the cone")
    # else:
    #     print("nothing to eat")


# num1 = int(input("Please enter number 1: "))
# num2 = int(input("Please enter number 2: "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#     print(f"{num2} is greater than {num1}")
# else:
#     print(f"Both numbers are equal")

num=int(input("please provide a any number:-"))
if num%2==0:
    print("even numbers")
else :
    print("odd numbers")

        

year = int(input("Enter your year: "))

if year % 100 == 0 and year % 400 == 0:
    print("It is a leap year")
elif year % 100 != 0 and year % 4 == 0:
    print("It is a leap year")
else:
    print("A normal year")







