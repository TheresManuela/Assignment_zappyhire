string=input("enter the string:")
print(string)
vowels=['a','e','i','o','u','A','E','I','O','U']
result=""
for i in range (len(string)):
    if string[i] not in vowels:
        result=result + string[i]
print("Result after removing vowels:",result)
