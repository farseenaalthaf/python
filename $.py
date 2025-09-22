str=input("enter a string")
string=str[0]
for i in range(1,len(str)):
  if str[i]!=str[0]:
    string=string+str[i]
  else:
    string=string+"$"
print(string)
