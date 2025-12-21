class Calculator:
    # Class to demonstrate method overloading using *args.
    def add(self, *args):
        # Add multiple numbers.
        result = 0
        for number in args:
            result += number
        return result

    def multiply(self, *args):
        # Multiply multiple numbers.
        result = 1
        for number in args:
            result *= number
        return result

# Main function to demonstrate method overloading
def main():
    calc = Calculator()

    # Using add method with different number of arguments
    print("Addition:")
    print(f"Sum of 5 and 3: {calc.add(5, 3)}")
    print(f"Adding 1, 2, 3, 4: {calc.add(1, 2, 3, 4)}")
    print(f"Adding 10, 20, 30, 40, 50: {calc.add(10, 20, 30, 40, 50)}")

    # Using multiply method with different number of arguments
    print("\nMultiplication:")
    print(f"Multiplication of 5 and 3: {calc.multiply(5, 3)}")
    print(f"Multiplying 1, 2, 3, 4: {calc.multiply(1, 2, 3, 4)}")
    print(f"Multiplying 10, 5, 2: {calc.multiply(10, 5, 2)}")

# Entry point of the program
if __name__ == "__main__":
    main()
