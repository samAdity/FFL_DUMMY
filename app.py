def divide_numbers(a, b):
    if b == 0:
        return None
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None
    return a / b

def main():
    numbers = [10, 0, 5, "text", 2]
    for num in numbers:
        result = divide_numbers(100, num)
        if result is not None:
            print(f"Result: {result}")
        else:
            print(f"Error: Cannot divide by {num}")

if __name__ == "__main__":
    main()