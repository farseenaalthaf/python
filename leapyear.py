current_year=2025
final_year=int(input("enter a year"))
for i in range(current_year,final_year):
 if((i%4)==0):
  if(i%100!=0):
   print(i)
   if((i%400)==0):
    print(i)
   
