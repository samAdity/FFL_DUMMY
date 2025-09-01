def divide_numbers(a, b):
    if b == 0:
        return float('inf')
    return a / b

def main():
    numbers = [10, 0, 5, "text", 2]
    for num in numbers:
        try:
            if not isinstance(num, (int, float)):
                print(f"Skipping invalid value: {num}")
                continue
            result = divide_numbers(100, num)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error processing {num}: {e}")

if __name__ == "__main__":
    main()