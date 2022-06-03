# play with lambda

def add():
    num=int(input("Enter a number from user:"))
    num1=int(input("Enter a second number:")) # here we have to take it 25 as given in question
    output=(lambda num,num1:num+num1) 
    return(output(num,num1))

result=add()
print("The addition of entered number and '25' is given by:",result)









