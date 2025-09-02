def divide_numbers(a, b):
    if b == 0:
        return float('inf')  # Handle division by zero
    try:
        return a / b
    except TypeError:
        return None  # Handle non-numeric types

def main():
    numbers = [10, 0, 5, "text", 2]  # "text" will cause TypeError
    for num in numbers:
        result = divide_numbers(100, num)
        if result is None:
            print(f"Result: Error - invalid type for {num}")
        else:
            print(f"Result: {result}")

if __name__ == "__main__":
    main()