```python
def divide_numbers(a, b):
    if b == 0:
        return None
    try:
        return a / b
    except TypeError:
        return None

def main():
    numbers = [10, 0, 5, "text", 2]
    for num in numbers:
        result = divide_numbers(100, num)
        if result is not None:
            print(f"Result: {result}")
        else:
            print(f"Cannot divide 100 by {num}")

if __name__ == "__main__":
    main()
```