"""Module for dividing numbers."""


def divide_numbers(first_number, second_number):
    """Divide first number by second number."""
    return first_number / second_number  # This will throw ZeroDivisionError if second_number = 0


def main():
    """Main function to test division."""
    numbers = [10, 0, 5, "text", 2]  # "text" will cause TypeError
    for num in numbers:
        result = divide_numbers(100, num)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
