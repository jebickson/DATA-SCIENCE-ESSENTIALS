# Function to write and read a text file
def text_file_operations():
    # Writing to a text file
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a sample text file.\n")
        file.write("Python file handling is easy!")

    # Reading from the text file
    with open("example.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)

# Function to write and read a binary file
def binary_file_operations():
    # Writing to a binary file
    data = bytearray([100, 200, 150, 50, 75, 30, 255])
    with open("example.binary.bin", "wb") as bin_file:
        bin_file.write(data)

    # Reading from a binary file
    with open("example.binary.bin", "rb") as bin_file:
        print("\nReading from binary file:")
        binary_content = bin_file.read()  # Fixed: was incorrectly using 'file.read()'
        print(f"Binary Content: {list(binary_content)}")

# Main function to run the file operations
def main():
    text_file_operations()       # Demonstrate text file operations 
    binary_file_operations()     # Demonstrate binary file operations

# Run the program
if __name__ == "__main__":
    main()
