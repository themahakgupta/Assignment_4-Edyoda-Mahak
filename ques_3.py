# write a python program to print the square of elements of list using map function

list_value=int(input("Enter the value:"))
lst=[]
for i in range(list_value):
    data=int(input("Enter your data:"))
    lst.append(data)
print("The guven list from user is:",lst)
def square(lst):
    return lst**2
square_output=list(map(square,lst))
print("The square of entered list is:", square_output)


