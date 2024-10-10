def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    print("Welcome to the Enhanced Calculator")
    
    # First input
    x = get_number("Please enter the first number: ")
    
    # Second input
    y = get_number("Please enter the second number: ")
    
    # Operation selection
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            break
        print("Invalid choice. Please try again.")
    
    if choice == '1':
        result = x + y
        operation = "+"
    elif choice == '2':
        result = x - y
        operation = "-"
    elif choice == '3':
        result = x * y
        operation = "*"
    elif choice == '4':
        if y != 0:
            result = x / y
            operation = "/"
        else:
            return "Error: Division by zero"
    
    return f"{x} {operation} {y} = {result}"

# Run the calculator
print(calculator())
