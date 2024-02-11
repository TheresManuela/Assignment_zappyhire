def reverse(my_tuple):
    reverse_items=[]
    for item in my_tuple:
        if isinstance(item,str):
            reverse_items.append(item[::-1])
        elif isinstance(item, (int,float)):
            reverse_items.append(str(item)[::-1])
        else:
            reverse_items.append(item)
        return tuple(reverse_items)
my_tuple=("abc",345,"program",21)
reverse_tuple=reverse(my_tuple)
print(reverse_tuple)