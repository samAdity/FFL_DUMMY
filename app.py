def divide_numbers(a, b):
    if b == 0:
        return 0
    return a / b

def main():
    numbers = [10, 0, 5, "text", 2]
    for num in numbers:
        if isinstance(num, (int, float)):
            result = divide_numbers(100, num)
            print(f"Result: {result}")
        else:
            print(f"Skipping invalid input: {num}")

if __name__ == "__main__":
    main()
