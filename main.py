print("hello world")

#hi i am sonia bilal i am from gujranwala
""""    this is multiple comment
krne ka tariqa but this is not a comment this is a doc string
 jis ma multiple para ko hm store kr skty ha


 """

#  declare variable 
name="sonia"
name1="bilal"
# dont use this due to declare variable
# 1name=""
# nam es=""
# $hi=""
a=34
b=23.4
c=12 / 2
print(type(b))
# data type string

string="heloo"
# data type booleans
bolean=True
# string indexing
a="hello"
print(a[3])
# string slicing 
#  eg - a = “hello” a[1:4:1] ==> output “ell:
b="hello world"
# print(a[1:3:1])
# ye end point tk jaye ga
# print (b[5::]) 
# ye 0 sae lekr end tk print kry ga
print (b[::])

""""type conversion yani ek type ko dosri type ma change krna"""
# int to string 
# a=12
# a=str(a)
# print(type(a))
# string to int
# a = "coder"
# a = int(a)  # ❌ Error: "coder" is not a number
# print(type(a))

a = "123"
a = int(a)  # ✅ Works fine
print(type(a))  # <class 'int'>

a = "decoder"
try:
    a = int(a)
    print(type(a))
except ValueError:
    print("Conversion failed: Not a number")

    """"boolean values conversions"""
    c=0
    print(bool(c))

# input and output
names="python coder"
age="23"
# print("my name is ",names,"and my age is",age)
# es code ko hm format string ma use kry gy
print(f"my name is {names} and my age is {age}")

# input and output 

input("Enter your name: ")
print("Hello,", name)

