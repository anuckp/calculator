x=int(input("enter the first num"))
y=int(input("enter the second num"))
z=input("enter the operator")

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
    
else:
    print("choose in between + - * /")
    
