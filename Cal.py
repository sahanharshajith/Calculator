while True:
    print("\nSelect operation.\n")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Factorial: ! ")
    print("7.Terminate: # \n")

    choice = str(input("Enter choice(+,-,*,/,^,%,!,#):"))
    if choice == '#':
            print('Done. Terminating')
            break
    print(choice)

    if choice in ('+','-','*','/','^','%','!','=','#'):

        if choice == '+':
            total_add = 0
            print('\nEnter "=" to finish\n')
            n = input('Enter a number:')
            while n != '=':
                try:
                    total_add = total_add + float(n)
                    n = input('Enter a number:')
                except ValueError:
                    print("Not a valid number.")
                    n = input('Enter a number:')
            print("The final result is:", total_add)

        elif choice == '-':
            total_sub = 0
            print('\nEnter "=" to finish\n')
            n = input('Enter a number:')
            while n != '=':
                total_sub = float(n)
                a = input('Enter a number:')
                try:
                    while a != '=':
                        total_sub = total_sub - float(a)
                        a = input('Enter a number:')
                    else:
                        print("The final result is:", total_sub)
                        break
                except:
                    print("Not a valid number.")
                    a = input('Enter a number:')
            else:
                print("The final result is:", total_sub)  

        elif choice == '*':
            total_multiply = 1
            print('\nEnter "=" to finish\n')
            n = input('Enter a number:')
            while n != '=':
                try:
                    total_multiply = total_multiply * float(n)
                    n = input('Enter a number:')
                except ValueError:
                    print("Not a valid number.")
                    n = input('Enter a number:')
            print("The final result is:", total_multiply)

        elif choice == '/':
            while True:
                try:
                    a = input("Enter first number:")
                    b = input("Enter second number:")
                    b = float(b)
                    if (b == 0):
                        print('Number division by zero')
                        print(a , '/' , b , '=' , 'Cannot divide by zero')
                        break
                    else:
                        print(a , '/' , b , '=' , (float(a) / b))
                        break
                except ValueError:
                        print("Not a valid number,please enter again")
                        continue
                
        elif choice == '^':
            while True:
                try:
                    a = input("Enter first number:")
                    b = input("Enter second number:")
                    print(a , '^' , b , '=' , (float(a) ** float(b)))
                    break
                except ValueError:
                    print("Not a valid number,please enter again")
                    continue

        elif choice == '%':
            while True:
                try:
                    a = input("Enter first number:")
                    b = input("Enter second number:")
                    print(a , '%' , b , '=' , (float(a) % float(b)) )
                    break
                except ValueError:
                    print("Not a valid number,please enter again")
                    continue
            
        elif choice == '!':
            factorial = 1
            while True:
                try:
                    n = input("Enter a number to find factorial:")
                    for i in range(1,int(n)+1):
                        factorial = factorial*i
                    print("The final result is:", factorial)
                    break
                except ValueError:
                    print("Not a valid number,please enter again")
                    continue
    else:
        print("Unrecognized operation")
        continue

print("Thank you for using this program.")
input("Press Enter to exit...")