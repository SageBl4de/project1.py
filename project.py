def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):      
    return a / b

print("Function Calculator")
print(" 1) Add \n 2) Substract \n 3) Multiply \n 4) Divide")
choice = input("What do you want to choose to do? (1/2/3/4) : ")    

try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("Result:", result)
        elif choice == '2':
            result = subtract(num1, num2)
        print("result:", result)

        elif choice == '2':
        result = multiply(num1, num2)
        print("result:", result)

        elif choice == '4':
        result = divide(num1, num2)
        print("result:", result)

        else:
        print("Invalid choice.")

except ZeroDivisionError:
    print("Error =  Dividing by zero is prohibited. ")

except ValueError:
    print("Error = You can only enter numbers!")