list1=[1,2,3,4,5]
list2=[6,7,8,9,5]
if len(list1)==len(list2):
  print("list1 and list2 are of same length")
else:
  print("list1 and list2 are of different length")
if sum(list1)==sum(list2):
    print("sum is equal")
else:
  print("sum is not equal")
for i in list1:
    if i in list2:
        print(i,"occurs in both lists")
    
