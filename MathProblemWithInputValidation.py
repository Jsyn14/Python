#write a program that will perform the four basic arithmetic operations using arguments
#syntax for defining a function - task # create the function
def task1(number1, number2):
    print("-------------------------------")
    return (number1 + number2)
def task2(number1, number2):
    print("-------------------------------")
    return (number1 - number2)
def task3(number1, number2):
    print("-------------------------------")
    return (number1 * number2)
def task4(number1, number2):
    print("-------------------------------")
    return (number1 / number2)
def task5(number1, number2):
    print("this task 5 will perform the following steps")    
def main(): #function name
    # body of the function
    print("==============================================")
    print("CIS202 Problem with input validation functions")
    print("==============================================")
    print(" Below are the listed options to be performed in this program.") 
    print(" 1. task 1 preforms addition")
    print(" 2. task 2 preforms subtraction")
    print(" 3. task 3 prefoms multiplcation")
    print(" 4. task 4 preforms division")
    print(" 5. task 5 Exits program")

# task #2 - call the function to display a menu of items
# the statement below will call the function
while True:
    main()
    option =int(input('Please enter a number from 1-5 ( 5 to exit)\t'))
    #check to determine which option was entered
    if option == 1:
        print("you selected option 1 Addition")
        number1 =int(input('Enter first number:\t'))
        print("                      +")
        number2 =int(input('Enter second number:\t'))              
        sum = task1(number1, number2)
        print("The sum of", number1,"+", number2,"=", sum)
    elif option == 2:
        print("you selected option 2 Subtraction")
        number1 =int(input('Enter first number:\t'))
        print("                      -")
        number2 =int(input('Enter second number:\t'))
        diff = task2(number1,number2)
        print("The difference", number1, "-", number2, "=", diff)
    elif option == 3:
        print("you selected option 3 Multiplcation")
        number1 =int(input('Enter first number:\t'))
        print("                      x")
        number2 =int(input('Enter second number:\t'))
        product = task3(number1,number2)
        print("The product of", number1, "X", number2, "=", product)
    elif option == 4:
        print("you selected option 4 Division")
        number1 =int(input('Enter first number:\t'))
        print("                        /")
        number2 =int(input('Enter second number:\t'))
        if number2 == 0:
            print('invalid number')
        else:
            quotient = task4(number1, number2)
            print("The quotient of", number1, "/", number2, "=", quotient)
    elif option == 5:
        print("Exit Program")
        break
    else:print("invalid option, enter a valid option from the list above(1-5)")
    if number2 == 0:
        print('ERROR: Second number cannot be divided by zero.')
        number2 = float(input('Enter the correct number ' +'a number that is not zero: '))
        print(number1 / number2)
        def task4(number1, number2):
             return (number1 / number2)
