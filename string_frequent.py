string=input("enter the string:")
print(string)
repeat={}
for i in string:
    if i in repeat:
       repeat[i]=repeat[i]+1
    else:
        repeat[i]=1
result=max(repeat, key = repeat.get)
print("most repeating letter is:",result) 