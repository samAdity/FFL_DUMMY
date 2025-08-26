def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"  # Handle division by zero
    return a / b

def main():
    numbers = [10, 0, 5, "text", 2]  # "text" will cause TypeError
    for num in numbers:
        try:
            result = divide_numbers(100, num)
            print(f"Result: {result}")
        except TypeError:
            print(f"Error: Invalid input '{num}' for division.")

if __name__ == "__main__":
    main()
