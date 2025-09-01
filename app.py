def divide_numbers(a, b):
    if b == 0:
        return 0  # Handle division by zero
    return a / b

def main():
    numbers = [10, 0, 5, "text", 2]
    for num in numbers:
        try:
            if isinstance(num, (int, float)):
                result = divide_numbers(100, num)
                print(f"Result: {result}")
            else:
                print(f"Skipping non-numeric value: {num}")
        except Exception as e:
            print(f"Error processing {num}: {e}")

if __name__ == "__main__":
    main()