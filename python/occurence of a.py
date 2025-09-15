list=["anu","meena","rani","anand"]
count=0
for i in list:
    print("occurence of a in",i,i.count("a"))
    count=count+i.count("a")
print("total number of a is",count)    
