def divide_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    numbers = [10, 0, 5, "text", 2]  # "text" will cause TypeError
    for num in numbers:
        try:
            result = divide_numbers(100, num)
            print(f"Result: {result}")
        except (ValueError, TypeError) as e:
            print(f"Error with {num}: {e}")

if __name__ == "__main__":
    main()
