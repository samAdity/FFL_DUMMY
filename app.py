"""Module for number division operations."""


def divide_numbers(first_number, second_number):
    """Divide two numbers and return the result."""
    return first_number / second_number  # This will throw ZeroDivisionError if b = 0


def main():
    """Main function to demonstrate division operations."""
    numbers = [10, 0, 5, "text", 2]  # "text" will cause TypeError
    for num in numbers:
        result = divide_numbers(100, num)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()