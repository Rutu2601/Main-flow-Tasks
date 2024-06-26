#TASK1 Arithmetic operation and conditional statements 

def main():
    print("Please select operation -")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice for calculation 1, 2, 3, 4: ")

    n1 = int(input("Enter value of number 1: "))
    n2 = int(input("Enter value of number 2: "))

    if choice == '1':
        print(n1,"+", n2,"=", n1+n2)

    elif choice == '2':
        print(n1,"-", n2,"=", n1-n2)

    elif choice == '3':
        print(n1,"*", n2,"=", n1*n2)

    elif choice == '4':
        if n2 != 0:
            print(n1,"/", n2,"=", n1/n2)
        else:
            print("Error! Division by zero.")
            
    else:
        print("Invalid choice")

main()
