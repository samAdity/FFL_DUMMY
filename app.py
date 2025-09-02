def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    try:
        return a / b
    except TypeError:
        return "Error: Invalid number type"

def main():
    numbers = [10, 0, 5, "text", 2]  # "text" will cause TypeError
    for num in numbers:
        result = divide_numbers(100, num)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()