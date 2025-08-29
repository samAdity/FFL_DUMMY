```python
def divide_numbers(a, b):
    if b == 0:
        return None
    return a / b

def main():
    numbers = [10, 0, 5, 2]
    for num in numbers:
        if isinstance(num, (int, float)):
            result = divide_numbers(100, num)
            if result is not None:
                print(f"Result: {result}")
            else:
                print("Error: Division by zero")
        else:
            print(f"Error: Invalid type for {num}")

if __name__ == "__main__":
    main()
```