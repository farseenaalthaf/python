s=input("enter a string")
if s[-3:]=="ing":
 s=s[:-3]+"ly"
else:
 s=s+"ing"
print("string is",s)
