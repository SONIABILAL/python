# two types of loop
# for loop some examples
# a=range(20,51,1)
# for i in a:
#     print(i)
# es code ko hm es tarah sae b likh skty ha

# for i in range(20,51,1):
#     print(i)
# agr hm ny 16 sae sae 1 tk jana ha tu hm 
for i in range(16,0,-1):
    print(i)
# lets write a table 5
# for table in range(5,51,5):
#     print(table)

# n=int(input("which table you want"))
# for i in range(n,(n*10)+1,n):
#     print(i)

    # /string ka use  in loops
# name="sonia"
# for i in range(5):
#     print(name[i])

name="hello i am a frontened developer"
for i in range(len(name)):
    print(name[i])

    # coninue and break
    # for i in range(20):
    #     if i==15:
    #         break
    #     else:
    #         print(i
    for i in range(20):
            if i==15:
                  print("continue statement is executed")
                  continue
            print(i)
            
            
    else:
            print("continue statement is not excuted")
    
# for loops questions with answers
# Accept an integer and Print hello world n times
# Accept an integer from the user
# n = int(input("Enter a number: "))

# Print "Hello World" n times
# for i in range(n):
#     print("Hello World")
# - Print natural number up to n 
# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     print(i)

#     n = int(input("Enter a number: "))
    # Reverse for loop. Print n to 1 
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)


#  Take a number as input and print its table 
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
# - Sum up to n terms 
       
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum up to", n, "terms is:", total)
# factorial numbers
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is:", factorial)
# even and odd numbers ka sum
n=int(input("tell your number"))
even=0
odd=0
for i in range(1,n+1):
     if i%2==0:
          even=even+i
     else:
          odd=odd+i
          print(f"even is {even} and odd is {odd}")
