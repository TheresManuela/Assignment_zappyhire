def large(list):
    max=list[0]
    for i in list:
        if i > max:
            max=i
    return max
list=[46,389,2222,7]
print("Largest number:",large(list))
