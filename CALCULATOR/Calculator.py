import calc
choice=0
flag=True
while(flag):
    print("\n SIMPLE CALCULATOR")
    print("Choose operation:\n 1.Add\n 2.Subtract\n 3.Multiply\n 4.Divide\n 5.Modulus\n 6.Square\n 7.Exit")
    choice=int(input("Enter your choice: "))
    if choice ==6:
        x=int(input("Enter the value of x: "))
        print("Result:",calc.square(x))
    elif choice == 7:
        flag=False
    else:
        x=int(input("Enter the value of x: "))
        y=int(input("Enter the value of y: "))
        match choice:
            case 1:
                print("Result:",calc.add(x,y))
            case 2:
                print("Result:",calc.subtract(x,y))
            case 3:
                print("Result:",calc.multiply(x,y))
            case 4:
                print("Result:",calc.divide(x,y))
            case 5:
                print("Result:",calc.modulus(x,y))
            case _:
                print("Invalid choice")

