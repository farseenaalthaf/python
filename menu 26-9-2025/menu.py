while True:
    print("-----------MENU------------")
    print("1.occurence of word\n 2.character frequency\n 3.factors of number\n 4EXIT")
    choice=int(input("enter a choice"))
    if(choice==1):
      text=input("enter a string")
      list=[]
      words=text.split()
      for word in words:
          if word in list:
              continue
          else:
              list.append(word)
              print("occurence of word",word,"in string=",words.count(word))
      continue
    if(choice==2):
      word=input("enter word")
      list1=[]
      for letter in word:
         if letter in list1:
          continue
         else:
          list1.append(letter)
          print("character frequency in",letter,"is",word.count(letter))
      continue
    if(choice==3):
        num=int(input("enter a number"))
        limit=int(input("enter the limit"))
        for i in range(1,limit):
            if(num%i==0):
             print(i)
        continue
    if(choice==4):
        break
    else:
        print("INVALID CHOICE TRY AGRAIN")
        continue
          
          
    

