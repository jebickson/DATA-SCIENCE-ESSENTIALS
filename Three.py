# Coding
# String Manipulation Program

def string_operations():
    # Function to demonstrate string manipulation.

    # Input a string from the user
    user_string = input("Enter a string: ")

    # 1. CONVERT TO UPPERCASE AND LOWERCASE
    print(f"\nOriginal String: {user_string}")
    print(f"Uppercase: {user_string.upper()}")
    print(f"Lowercase: {user_string.lower()}")

    # 2. REVERSE THE STRING
    reversed_string = user_string[::-1]
    print(f"Reversed String: {reversed_string}")

    # 3. Count the occurrences of a specific character
    char_to_count = input("Enter a character to count its occurrences: ")
    count = user_string.count(char_to_count)
    print(f"The character '{char_to_count}' occurs {count} time(s).")

    # 4. Replace a substring with another substring
    old_substring = input("\nEnter the old substring to replace: ")
    new_substring = input("Enter the new substring: ")
    replaced_string = user_string.replace(old_substring, new_substring)
    print(f"Modified String: {replaced_string}")

    # 5. Check if the string is a palindrome
    is_palindrome = user_string == reversed_string
    print(f"Is the string a palindrome? {'Yes' if is_palindrome else 'No'}")

    # 6. Split the string into words
    words = user_string.split()
    print(f"\nWords in the string: {words}")

    # 7. Join the words with a specific delimiter
    delimiter = input("\nEnter a delimiter to join the words: ")
    joined_string = delimiter.join(words)
    print(f"Joined String: {joined_string}")

    # 8. Strip leading and trailing spaces
    stripped_string = user_string.strip()
    print(f"\nString without leading/trailing spaces: '{stripped_string}'")

    # 9. Find the position of a substring
    substring_to_find = input("\nEnter a substring to find its position: ")
    position = user_string.find(substring_to_find)
    if position != -1:
        print(f"'{substring_to_find}' found at position {position}.")
    else:
        print(f"'{substring_to_find}' not found in the string.")

    # 10. Check if the string starts and ends with specific substrings
    start_substring = input("\nEnter a starting substring to check: ")
    end_substring = input("Enter an ending substring to check: ")
    print(f"Does the string start with '{start_substring}'? {'Yes' if user_string.startswith(start_substring) else 'No'}")
    print(f"Does the string end with '{end_substring}'? {'Yes' if user_string.endswith(end_substring) else 'No'}")

# Call the string manipulation function
if __name__ == "__main__":
    string_operations()
