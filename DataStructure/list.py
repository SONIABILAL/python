a=[1,2,3,4,5,6,4,print(),"hello"]
print (a)
# modified the values
a[2]=5
print(a)
# print(a[0:5]) slice methods
print(a[-1])

# traversing methods
# 1st way using index
# b=[12,13,45,67,88]
# for i in range(len(b)):
#     print(b[i])
    # 2nd way directly values
b=[12,13,45,67,88]
for i in b:
 print(i)

#  print(dir(list))
#  help(list)
# to use different methods
l=[1,2,3,4,5,6,7]
# l.append(2)
l.insert(1,3)
l.remove(5)
print(l)

# queations on lists 
# print positive and negative elements  seprately
l=[12,23,-34,-56,78] 
for i in l:
 if i>=0:
  print(f"positive elemnts are {i}")
for i in l:
 if i<0:
  print(i)
# means the list of elemnts
l=[12,2234,4,567,67,890]
sum=0
for i in l:
 sum=sum+i
print(sum/len(l))
# find the largest number and its index too
l=[234,56,1234,57,998]
largest=l[0]
index=0
for i in range(len(l)):
 if l[i] > largest:
  largest=l[i]
  index=i
print(f"your largest number is {largest} and index is {index}")
# find the second largest numbers

l = [234, 56, 1234, 57, 998, 5]
largest = l[0]
secLargest = float('-inf')  # Start with very small number

for i in l:
    if i > largest:
        secLargest = largest
        largest = i
    elif i > secLargest and i != largest:
        secLargest = i

print(f"Second largest: {secLargest}, Largest: {largest}")

   
 


