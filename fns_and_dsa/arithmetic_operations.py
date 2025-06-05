def perform_operation(num1, num2, operation):
    result = 0
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            print("Error: cannot divide by zero")
            return None
        result = num1 / num2 
    else:
        print("Error: Unknown operation")
    return result
if __name__ == "__main__":
    num1 = 10.0
    num2 = 4.2
    operation = 'add'
    print(f"The Result is: {perform_operation(num1, num2, operation)}")