string=input("enter the string:")
string=string.casefold()
reverse_string=reversed(string)
if list(string) == list(reverse_string):
    print("palindrome")
else:
    print("not palindrome")