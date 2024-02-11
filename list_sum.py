list=[34,65,22,100]
temp=[]
for i in list:
    sum=0
    for digit in str(i):
        sum=sum + int(digit)
    temp.append(sum)
print("the sum is:",str(temp))