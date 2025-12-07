def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a % b

def power(a, b):
    return a ** b

def calculator():
    print("=== WELCOME TO THE INTERACTIVE CALCULATOR ===")
    
    while True:
        print("\nAvailable operations:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Modulo (%)")
        print("6. Power (^)")
        print("7. Exit")
        
        choice = input("Select an operation (1-7): ")
        
        if choice == "7":
            print("Goodbye!")
            break
        
        if choice not in ["1","2","3","4","5","6"]:
            print("Invalid choice, try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number, please enter numeric values.")
            continue
        
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "5":
            result = modulo(num1, num2)
        elif choice == "6":
            result = power(num1, num2)
        
        print(f"Result: {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()
