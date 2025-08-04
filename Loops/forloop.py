# two types of loop
# for loop some examples
a=range(20,51,1)
for i in a:
    print(i)
# es code ko hm es tarah sae b likh skty ha

# for i in range(20,51,1):
#     print(i)
# agr hm ny 16 sae sae 1 tk jana ha tu hm 
# for i in range(16,0,-1):
#     print(i)
# lets write a table 5
# for table in range(5,51,5):
#     print(table)

n=int(input("which table you want"))
for i in range(n,(n*10)+1,n):
    print(i)

    # /string ka use  in loops
# name="sonia"
# for i in range(5):
#     print(name[i])

# name="hello i am a frontened developer"
# for i in range(len(name)):
#     print(name[i])

    # coninue and break
for i in range(20):
        if i==15:
            break
        else:
            print("else some thing")
            # continues
for i in range(20):
            if i==15:
                  print("continue statement is executed")
                  continue
            print(i)
            
            
else:
            print("continue statement is not excuted")
    







 






         