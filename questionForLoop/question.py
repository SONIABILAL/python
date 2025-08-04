      # Accept an integer and Print hello world n times
# Accept an integer from the user
n = int(input("Enter a number: "))

# Print "Hello World" n times
for i in range(n):
    print("Hello World")

    
# - Print natural number up to n 
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)

    n = int(input("Enter a number: "))
    # #  Take a number as input and print its table 
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    # Reverse for loop. Print n to 1 
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)
#   - Print all the factors of a number 
factors = int(input("Which number's factors you want: "))
for i in range(1, factors + 1):
    if factors % i == 0:
        print(i)
print("hello")

#  even and odd numbers ka sum
n=int(input("tell your number"))
even=0
odd=0
for i in range(1,n+1):
     if i%2==0:
          even=even+i
     else:
          odd=odd+i
          print(f"even is {even} and odd is {odd}")

          # check your number is perfect or not
n = int(input("Check if your number is perfect or not: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("Your number is perfect.")
else:
    print("Your number is not perfect.")

    # check number is prime or not
    n = int(input("Check if your number is prime or not: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("This is a prime number.")
else:
    print("This is not a prime number.")

    # # factorial numbers
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is:", factorial)
       #  Reverse a string without using in build functions.
name="sonia"
b=""
for i in range(len(name)-1,-1,-1):
    b=b+name[i]
    print(b)

       # check it is palindrom is not
name="121"
b=""
for i in range(len(name)-1,-1,-1):
    b=b + name[i]



if b==name:
    print("it is palindrom")
else:
        print("it is not palindrom")
        # check different chracters
        a = "sobasdf12356@#$%"
digit = 0
specChr = 0
chr = 0

for i in a:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        chr += 1
    else:
        specChr += 1

print(f"Your digits are {digit}, your special characters are {specChr}, and your letters are {chr}.")


# - Sum up to n terms 
       
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum up to", n, "terms is:", total)