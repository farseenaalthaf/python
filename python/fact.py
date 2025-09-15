fact=1
num=int(input("enter a number"))
for i in range(num,1,-1):
    print(i,"*",end=" ")
    fact=fact*i
print(1,"=",fact)
print("factorial of num is",fact)
