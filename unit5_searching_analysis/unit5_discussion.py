"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    counter = 0; #set counter to 0 for code that desires to use it

    for i in range(len(lst)):
        counter += 1 # increment counter for code that desires it
        if (lst[i] == target):
            #print(f"Index: {i}, Comparisons: {counter}")
            #Commented out additional formatting logic
            return i

    #print(f"Index: -1, Comparisons: {counter}")
    # Commented out additional formatting logic
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    counter = 0 #set counter to 0 for code that desires it
    low = 0
    high = len(lst) - 1;

    while (high >= low):
        counter += 1 #increment counter for code that desires it
        mid = (high + low) // 2
        if (lst[mid] < target):
            low = mid + 1
        elif (lst[mid] > target):
            high = mid - 1
        else:
            #print(f"Index: {mid}, Comparisons: {counter}")
            # Commented out additional formatting logic
            return mid
    #print(f"Index: -1, Comparisons: {counter}") # not found
    # Commented out additional formatting logic
    return -1

def main():

    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.


    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    #Creating a small dataset
    cakewalk_numbers = [3, 5, 8, 16, 22, 27, 35]

    #Linear search for one present and one missing value
    print("Linear search for 8:",
          linear_search(cakewalk_numbers, 8))
    print("Linear search for 50:",
          linear_search(cakewalk_numbers, 50))

    # Binary search for one present and one missing value
    print("Binary search for 22:",
          binary_search(cakewalk_numbers, 22))
    print("Binary search for 21:",
          binary_search(cakewalk_numbers, 21))
    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # Defining a larger dataset
    big_dataset = list(range(1, 751))

    #Set a target value
    target = 333

    #Conducting a linear search
    print("Linear search:")
    print(linear_search(big_dataset, target))

    #Conducting a binary search
    print("Binary search:")
    print(binary_search(big_dataset, target))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    #Creating an empty list for edge cases
    empty_list = []
    print("Linear search on empty list:",
          linear_search(empty_list, 5))
    print("Binary search on empty list:",
          binary_search(empty_list, 5))

    # Creating a new sorted list for edge cases
    new_list = [1, 5, 11, 15, 21, 25,
                33, 42, 43, 47, 51]

    print("Binary search for first element:",
          binary_search(new_list, 1))

    print("Binary search for last element:",
          binary_search(new_list, 51))

if __name__ == "__main__":
    main()