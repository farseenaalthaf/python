def number():
    while(True):
        n=int(input("enter a number greater than 1000"))
        if n<=1000:
            print("the numbner is less than 1000")
            continue
        else:
            break
    return n
def rev(n):
    length=len(str(n))
    rev=0
    for i in range(length):
      mod=n%10
      n=n//10
      rev=(rev*10)+mod
    return rev
input_number=number()
reverse_number=rev(input_number)
print(input_number)
print(reverse_number)
    
