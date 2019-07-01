x=int(input("Enter the first num: "))
y=int(input("Enter the second num: "))
while True:
    z=input("Enter the operator: ")
    if z=='+':
        result=x+y
        print(result)
        break

    elif z=='-':
        result=x-y
        print(result)
        break
    
    elif z=='*':
        result=x*y
        print(result)
        break
    
    elif z=='/':
        result=x/y
        print(result)
        break
    elif z=='%':
        result=x%y
        print(result)
        break
    else:
        print("choose in between + - * /")
    
