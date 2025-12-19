#Coding
def dictionary_operations():
    # Function to demonstrate dictionary creation and manipulation.

    # 1. Create dictionaries
    print("Creating Dictionaries:")
    empty_dict = {}
    simple_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    nested_dict = {'person': {'name': 'Bob', 'age': 25}, "job": "Engineer"}

    print(f"Empty Dictionary: {empty_dict}")
    print(f"Simple Dictionary: {simple_dict}")
    print(f"Nested Dictionary: {nested_dict}")

    # 2. Accessing elements
    print("\nAccessing Elements:")
    print(f"Name: {simple_dict['name']}")
    print(f"Age: {simple_dict.get('age')}")
    print(f"Job from Nested Dictionary: {nested_dict['job']}")

    # 3. Adding and updating elements
    print("\nAdding and Updating Elements:")
    simple_dict['country'] = "USA"
    print(f"After adding 'country': {simple_dict}")
    simple_dict['age'] = 26  # Updating existing key
    print(f"After updating 'age': {simple_dict}")

    # 4. Removing elements
    print("\nRemoving Elements:")
    removed_value = simple_dict.pop('city')
    print(f"Removed 'city': {removed_value}")
    print(f"Dictionary after removal: {simple_dict}")
    del simple_dict["country"]  # removing using del
    print(f"Dictionary after deleting 'country': {simple_dict}")

    # 5. Looping through dictionary
    print("\nLooping Through Dictionary:")
    print("Keys:")
    for key in simple_dict.keys():
        print(key)
    print("Values:")
    for value in simple_dict.values():
        print(value)
    print("Key-Value Pairs:")
    for key, value in simple_dict.items():
        print(f"{key}: {value}")

    # 6. Checking membership
    print("\nMembership Test:")
    print(f"Is 'name' a key in the dictionary? {'Yes' if 'name' in simple_dict else 'No'}")
    print(f"Is 'Alice' a value in the dictionary? {'Yes' if 'Alice' in simple_dict.values() else 'No'}")

    # 7. Length of dictionary
    print("\nDictionary Length:")
    print(f"Number of elements in dictionary: {len(simple_dict)}")

    # 8. Merging dictionaries
    print("\nMerging Dictionaries:")
    new_dict = {'hobby': 'Reading', "language": "Python"}
    simple_dict.update(new_dict)
    print(f"After merging with new data: {simple_dict}")

    # 9. Dictionary comprehension
    print("\nDictionary Comprehension:")
    squared_dict = {x: x**2 for x in range(1, 6)}
    print(f"Squared Numbers Dictionary: {squared_dict}")

    # 10. Working with nested dictionaries
    print("\nWorking with Nested Dictionaries:")
    print(f"Nested Dictionary: {nested_dict}")
    print(f"Accessing Nested Element (Name): {nested_dict['person']['name']}")
    nested_dict['person']['age'] = 35
    print(f"Updated Nested Dictionary: {nested_dict}")

# Call the dictionary operations function
if __name__ == "__main__":
    dictionary_operations()
