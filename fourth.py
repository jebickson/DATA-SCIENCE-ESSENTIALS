# Tuple Creation and Manipulation

def tuple_operations():

    # 1. Create a tuple
    print("Creating Tuples:")
    empty_tuple = ()
    single_element_tuple = (42,)  # Note the comma for single element tuple
    multiple_element_tuple = (10, 20, 30, 40, 50)

    print(f"Empty Tuple: {empty_tuple}")
    print(f"Single Element Tuple: {single_element_tuple}")

    # 2. Accessing elements
    print("\nAccessing Elements:")
    print(f"First element: {multiple_element_tuple[0]}")
    print(f"Last element: {multiple_element_tuple[-1]}")

    # 3. Slicing a tuple
    print("\nSlicing Tuples:")
    print(f"Elements from index 1 to 3: {multiple_element_tuple[1:4]}")
    print(f"Elements from start to index 2: {multiple_element_tuple[:3]}")
    print(f"Elements from index 2 to end: {multiple_element_tuple[2:]}")

    # 4. Concatenation and repeating tuples
    print("\nConcatenation and Repeating Tuples:")
    new_tuple = multiple_element_tuple + (60, 70)
    print(f"Concatenated Tuple: {new_tuple}")
    repeated_tuple = single_element_tuple * 3
    print(f"Repeated Tuple: {repeated_tuple}")

    # 5. Checking membership
    print("\nMembership Test:")
    print(f"Is 20 in tuple? {'Yes' if 20 in multiple_element_tuple else 'No'}")
    print(f"Is 100 in tuple? {'Yes' if 100 in multiple_element_tuple else 'No'}")

    # 6. Finding length, max, and min
    print("\nTuple Statistics:")
    print(f"Length of tuple: {len(multiple_element_tuple)}")
    print(f"Max value in tuple: {max(multiple_element_tuple)}")
    print(f"Min value in tuple: {min(multiple_element_tuple)}")

    # 7. Tuple unpacking
    print("\nTuple Unpacking:")
    a, b, c, d, e = multiple_element_tuple
    print(f"Unpacked Values: a={a}, b={b}, c={c}, d={d}, e={e}")

    # 8. Converting a list to a tuple
    print("\nConverting List to Tuple:")
    sample_list = [1, 2, 3, 4, 5]
    converted_tuple = tuple(sample_list)
    print(f"Original List: {sample_list}")
    print(f"Converted Tuple: {converted_tuple}")

    # 9. Nested tuples
    print("\nNested Tuples:")
    nested_tuple = (1, 2, (3, 4), (5, 6))
    print(f"Nested Tuple: {nested_tuple}")
    print(f"Accessing element from nested tuple: {nested_tuple[2][0]}")  # Accessing 3

    # 10. Immutable nature of tuples
    print("\nImmutable Nature of Tuples:")
    try:
        multiple_element_tuple[0] = 100
    except TypeError as e:
        print(f"Error: {e} - Tuples are immutable and cannot be modified.")

# Call the tuple operations function
if __name__ == "__main__":
    tuple_operations()
