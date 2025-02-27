def add(a, b):
    return a + b
if __name__ == "__main__":
    print ("Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add(num1, num2)
    print(f"Result: {result}")