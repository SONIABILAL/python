s={1,2,3,4,5,4,5}

# duplicate words are not allowed
# sets ma hash value k hesab sae value store hoti ha
# set=hash("hello")
# print(set)
# print(s)

# es ma hmari values hash value k mutabaq store hoti ha
# a={1,2,3,5,6,9,7}
# for i in a:
#     print(i)
# different methods
set={1,2,3,4,56,6}
setA={5,1,2,3,5,6,8,9}
setB={12,2,4,5,6,7}
# set.add(4)
# set.remove(6)
# set.pop()
# set.clear()
# union
# setC=setA | setB
# intersection
# setC=setA.intersection (setB)
# setC=setA & setB
# setC=setB.difference (setA)
setC=setB - (setA)
# symmetric differcence
setC=setA ^ setB
setA -=setB



print(setC)

print(set)