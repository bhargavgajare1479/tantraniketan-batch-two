def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    try:
        result = factorial(num)
        print(f"Factorial of {num} is {result}")
    except ValueError as e:
        print(e)