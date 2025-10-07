length=int(input("enter length of word"))
words=[]
for i in range(0,length):
 word=input("enter a word")
 words.append(word)
large=""
for i in range(0,len(words)):
  if len(large)<len(words[i]):
    large=words[i]
print("length of longest word is",len(large))
