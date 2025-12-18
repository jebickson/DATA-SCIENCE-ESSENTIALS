# Function to greet a user
def greet_user(name):
    # Function to greet the user with their name
    print(f"Hello, {name}! Welcome to the Python programming world.")

# Function to calculate the sum of two numbers
def calculate_sum(a, b):
    # Function to calculate the sum of two numbers
    return a + b

# Function to find the factorial of a number
def factorial(n):
    # Recursive function to find factorial of a number
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function to check if a number is prime
def is_prime(num):
    # Function to check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to demonstrate variable-length arguments
def print_items(*items):
    # Function to print all items passed as arguments
    print("Items:")
    for item in items:
        print(f"- {item}")

# Main function to call other functions
def main():
    # Greet the user
    name = input("Enter your name: ")
    greet_user(name)

    # Calculate sum
    print("\nSum Calculation:")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The sum of {num1} and {num2} is {calculate_sum(num1, num2)}.")

    # Find factorial
    print("\nFactorial Calculation:")
    n = int(input("Enter a number to find its factorial: "))
    print(f"The factorial of {n} is {factorial(n)}.")

    # Check prime number
    print("\nPrime Number Check:")
    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

    # Demonstrate variable-length arguments
    print("\nPrint Items:")
    print_items("Apple", "Banana", "Cherry", "Date")

# Entry point of the program
if __name__ == "__main__":
    main()
