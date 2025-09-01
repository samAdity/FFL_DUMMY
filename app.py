def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Invalid input type"
    return a / b

def main():
    numbers = [10, 0, 5, "text", 2]
    for num in numbers:
        result = divide_numbers(100, num)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()