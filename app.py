"""Module for dividing numbers with error handling."""


def divide_numbers(first_number, second_number):
    """Divide two numbers with error handling."""
    if second_number == 0:
        raise ValueError("Cannot divide by zero")
    if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return first_number / second_number


def main():
    """Main function to demonstrate division with error handling."""
    numbers = [10, 0, 5, "text", 2]
    for num in numbers:
        try:
            result = divide_numbers(100, num)
            print(f"Result: {result}")
        except (ValueError, TypeError) as error:
            print(f"Error with {num}: {error}")


if __name__ == "__main__":
    main()
