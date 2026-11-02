"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    #Inserting into a list will cause values to shift if they are to the right of the inserted value, effecting
    #performance depending on the size of the list. This must be considered in applications handling large amounts
    #of data or where performance is critical.
    lst.insert(index, value)



def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    #Index validation prevents undefined behavior from occurring, and safe deletion of items ensures
    #that the list will continue to perform as expected - IE without the unintended loss of customer names.
    if index < 0 or index >= len(lst):
        print("The provided value must be within the range of the list.")
        return None
    else:
        return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    #This is a linear search because it takes a directional search from the lowest index to the highest, and has
    #utilized a for loop to cycle through each sequential index through the list.
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    #A list of names, called customers is initialized and displayed
    customers = ["Bob", "Ryan", "Savannah"]
    print("This is a list of customers: ", customers)

    #Adding a name to the beginning of the list is done using index 0
    print("The name Rosander will be added to the beginning:")
    insert_at(customers, 0, "Rosander")
    print(customers)

    #Adding a name to the middle of the list is done using index 3
    print("The name Evan will be added to the middle:")
    insert_at(customers, 2, "Evan")
    print(customers)

    #Adding a name to the end of the list is done using index 5
    print("The name Melinda will be added to the end:")
    insert_at(customers,5, "Melinda")
    print(customers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    print("Deleting one name from the beginning:")
    deletedName = delete_at(customers, 0)
    print("Deleted the customer:", deletedName)
    print(customers) #This new output is the current customers list with the first name removed

    print("Deleting one name from the middle:")
    deletedName = delete_at(customers, 2)
    print("Deleted the customer:", deletedName)
    print(customers) #This new output is the current customers list with a middle name removed

    print("Deleting one item from the end:")
    deletedName = delete_at(customers, len(customers)-1)
    print("Deleted the customer:", deletedName)
    print(customers) #This new output is the current customers list with the final name removed

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    #Searching whether the name Evan exists in the list
    #In either case, the program has control flow to handle existing or non-existing names.
    checkValue = search_value(customers, "Evan")
    if checkValue != -1:
        print("The name Evan was found at position: ", checkValue)
    else:
        print("The name Evan was not found.")

    #searching for a name that does not exist in the list
    checkValue = search_value(customers, "Billy")
    if checkValue != -1:
        print("The name Billy was found at position: ", checkValue)
    else:
        print("The name Billy was not found.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    #One edge case to delete something outside the range of the list
    print("Attempting to delete a name at position 9: ")
    delete_at(customers, 9) #The method handles this by warning the user that they exceeded the index bounds

    #One edge case to insert a new name into a position of an empty list
    species = []
    print("Attempting to insert an item into an empty list:")
    insert_at(species, 2, "Lizard")
    print(species) #The insertion is successful, however it defaults to position 0


if __name__ == "__main__":
    main()