def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def get_user_choice():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    return choice

def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def main():
    while True:
        choice = get_user_choice()
        
        if choice in ('1', '2', '3', '4'):
            num1, num2 = get_numbers()
            
            if choice == '1':
                result = add(num1, num2)
                print(f"The result of {num1} + {num2} is: {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"The result of {num1} - {num2} is: {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"The result of {num1} * {num2} is: {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Invalid input. Please select a valid operation.")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
