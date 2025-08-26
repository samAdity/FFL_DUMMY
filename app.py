def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"  # Handle division by zero
    return a / b

def main():
    numbers = [10, 0, 5, "text", 2]  # "text" will cause TypeError
    for num in numbers:
        try:
            result = divide_numbers(100, num)
            print(f"Result: {result}")
        except TypeError:
# <<<<<<< aiops/fix-20250826-090044
            print(f"Error: Invalid input '{num}', must be a number.")
# =======
#             print(f"Error: Invalid input '{num}' for division.")
# >>>>>>> aiops/fix-20250826-085944

if __name__ == "__main__":
    main()
