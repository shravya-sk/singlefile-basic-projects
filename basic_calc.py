def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    
    try:
        choice=int(input("Enter your choice:"))
        if choice<=0 or choice>4:
            print("enter a valid choice")
            break
        num1=int(input("enter a num1:"))
        num2=int(input("enter a num2:"))
        if choice==1:
            result=add(num1,num2)
            print(result)
        elif choice==2:
            result=sub(num1,num2)
            print(result)
        elif choice==3:
            result=mul(num1,num2)
            print(result)
        elif choice==4:
            result=div(num1,num2)
            print(result)
        break
    except ValueError as e:
        print(e)
    finally:
        print("thank you")