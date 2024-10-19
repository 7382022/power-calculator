
def calculate_power(base, exponent):
    return base ** exponent

# Get user input
try:
    base = float(input("Enter the base number (x): "))
    exponent = int(input("Enter the exponent (n): "))

    result = calculate_power(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")
except ValueError:
    print("Invalid input. Please enter numerical values.")

    