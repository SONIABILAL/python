# in buid functions
print("hello world")
# function create by your own
def greet():
    print("good morning")
greet()
# parameters and arguments
def sum(a,b):
    print(f"sum of  a  and b is {a+b}")
sum(5,8)
# key word arguments
def sum(a,b):
    print(f"sum of  a  and b is {a+b}")
sum(a=5,b=8)

# default arguments
def sum(a,b=9):
    print(f"sum of  a  and b is {a+b}")
sum(5,)

# pallindrom
def pallindrome(st):
    rev=""
    for i in range(len(st)-1,-1,-1):
        rev=rev+st[i]
        if rev==st:
            print("pallindrom")
        else:
            print("not a pallindrom")
pallindrome("namans")

# return
def hello():
    return "this is a hello function"
print(hello())
