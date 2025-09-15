l=[]
a=int(input('enter size'))
for i in range(0,a):
    num=int(input('enter numbers'))
    if num>100:
      l.append('over')
    else:
      l.append('num')
i=i+1
print(l)
