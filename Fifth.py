#coding
# List Creation and Manipulation

def list_operations():
    # Function to demonstrate list creation and manipulation.

    # 1. Create lists
    print("Creating Lists:")
    empty_list = []
    single_element_list = [42]
    multiple_element_list = [10, 20, 30, 40, 50]

    print(f"Empty List: {empty_list}")
    print(f"Single Element List: {single_element_list}")
    print(f"Multiple Element List: {multiple_element_list}")

    # 2. Accessing elements
    print("\nAccessing Elements:")
    print(f"First element: {multiple_element_list[0]}")
    print(f"Last element: {multiple_element_list[-1]}")

    # 3. Slicing a list
    print("\nSlicing Lists:")
    print(f"Elements from index 1 to 3: {multiple_element_list[1:4]}")
    print(f"Elements from start to index 2: {multiple_element_list[:3]}")
    print(f"Elements from index 2 to end: {multiple_element_list[2:]}")

    # 4. Adding and removing elements
    print("\nAdding and Removing Elements:")
    multiple_element_list.append(60)
    print(f"List after appending 60: {multiple_element_list}")
    multiple_element_list.insert(2, 25)
    print(f"List after inserting 25 at index 2: {multiple_element_list}")
    multiple_element_list.remove(30)
    print(f"List after removing 30: {multiple_element_list}")
    popped_element = multiple_element_list.pop()
    print(f"Popped element: {popped_element}")
    print(f"List after popping last element: {multiple_element_list}")

    # 5. Modifying elements
    print("\nModifying Elements:")
    multiple_element_list[0] = 5
    print(f"List after modifying first element to 5: {multiple_element_list}")

    # 6. Sorting and reversing
    print("\nSorting and Reversing:")
    multiple_element_list.sort()
    print(f"Sorted List: {multiple_element_list}")
    multiple_element_list.reverse()
    print(f"Reversed List: {multiple_element_list}")

    # 7. List comprehension
    print("\nList Comprehension:")
    squared_list = [x**2 for x in multiple_element_list]
    print(f"Squared List: {squared_list}")

    # 8. Checking membership
    print("\nMembership Test:")
    print(f"Is 20 in list? {'Yes' if 20 in multiple_element_list else 'No'}")
    print(f"Is 100 in list? {'Yes' if 100 in multiple_element_list else 'No'}")

    # 9. Length of list
    print("\nLength of List:")
    print(f"Length of list: {len(multiple_element_list)}")

    # 10. Converting a tuple to a list
    print("\nConverting Tuple to List:")
    sample_tuple = (1, 2, 3, 4, 5)
    converted_list = list(sample_tuple)
    print(f"Original Tuple: {sample_tuple}")
    print(f"Converted List: {converted_list}")

    # 11. Nested lists
    print("\nNested Lists:")
    nested_list = [1, 2, [3, 4, [5, 6]]]
    print(f"Nested List: {nested_list}")
    print(f"Accessing element from nested list: {nested_list[2][2][0]}")  # Accessing 5

# Call the list operations function
if __name__ == "__main__":
    list_operations()
