def calculator():
    ''' This is a function which when called do the calculation based operations which user wants '''

    x=int(input("Enter the first num: "))
    y=int(input("Enter the second num: "))

    z=input("Enter the operator: ")

    if z=='+':
        result=x+y
        print(result)

    elif z=='-':
        result=x-y
        print(result)
        
    elif z=='*':
        result=x*y
        print(result)
        
    elif z=='/':
        result=x/y
        print(result)
       
    elif z=='%':
        result=x%y
        print(result)

    elif z=='**':
        result=x**y
        print(result)
        
    else:
        print("Choose in between +,  -,  *,  /, **")
        

while True:
    i = int(input("Press 1 to Continue, otherwise press 0\n")) 
    if i == 1:
        calculator()
    else:
        break
