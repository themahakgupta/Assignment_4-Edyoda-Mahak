# write a python program to triple all numbers of a given list of integers using python map function

list_value=int(input("Enter the value:"))
lst=[]
for i in range(list_value):
    data=int(input("Enter your data:"))
    lst.append(data)
print("The entered list from user is:",lst)
def triple(lst):
    return lst*3
triple_output=list(map(triple,lst))
print("The square of entered list is:",triple_output)




