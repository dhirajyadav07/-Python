sentance=input("write a sentance; ")
count=0
flag=0
for i in sentance:
   if i.isalpha():
      flag=1
   elif flag:
      count +=1
      flag=0
if flag:
   count +=1
      
        
print(count)