"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None #Left and right nodes are initialized as None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None #All that is needed to initialize an empty BST is a None root.

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        #Call the recursive helper method.
        self.root = self._insert_recursive(self.root, value)



    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None: #Immediate placement of the node into the BST for an empty BST
            return Node(value)

        elif value < node.value: #Directs placement of the node to the left if < current node value
            node.left = self._insert_recursive(node.left, value)

        elif value > node.value: #Directs placement of the node to the right if > current node value
            node.right = self._insert_recursive(node.right, value)

        else: #For handling edge case that the value already is in the BST
            print("This value already exists in the tree!")

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        #Call the recursive helper method.
        return self._search_recursive(self.root, value)


    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if (node is None): #Handles the edge case of an empty BST
            return False
        elif (value == node.value): #The actual detection of the value the user desired
            return True
        elif (value < node.value): #Directing the search to the left subtree if the value is < current node value
            return self._search_recursive(node.left, value)
        elif (value > node.value): #Directing the search to the right subtree if the value is > current node value
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        #Use an empty list to store ordered values, and call the recursive helper method.
        ordered_values = []
        self._inorder_recursive(self.root, ordered_values)
        return ordered_values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node: #In order to only execute if a node exists
            self._inorder_recursive(node.left, values) #Traversing left subtree
            values.append(node.value) #Appending the node value
            self._inorder_recursive(node.right, values) #Traversing the right subtree
        return

def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    #Creating an empty BST
    guestnumbers = BST()
    #Preparing values to pass to the BST
    pendingnumbers = [30, 12, 28, 41, 9, 55, 45, 16]

    #Cycling through each pending number to add to our BST
    for number in pendingnumbers:
        guestnumbers.insert(number)

    #Printing the values we inserted
    print("Guest Numbers in insertion order:", pendingnumbers)
    #A Binary Search Tree is efficient at reducing search time because the structure of the tree encodes
    #additional relationships between the nodes for quicker access, which could not be seen encoded in
    #a structure such as a linked list.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    #Calling the inorder() method arranges our tree values in order. This is because the recursive method
    #first visits the left subtree, then the current node, and finally the right subtree. Manipulation of the
    #order and direction of these visits would result in other types of traversals.
    sorted_guests = guestnumbers.inorder()
    print("Sorted guest numbers:", sorted_guests)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    for number in [16, 45]: #Print the results of a search for 2 existing values.
        print(f"Was the guest number {number} found?: {guestnumbers.search(number)}")
    for number in [15, 22]: #Print the results of a search for 2 non-existing values.
        print(f"Was the guest number {number} found?: {guestnumbers.search(number)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    #Attempting  to insert a value that already exists in the tree. The insert recursive method will handle this
    #by detecting that the number already exists and printing an appropriate response, without modifying the BST.
    print("Inserting the number 30: ")
    guestnumbers.insert(30)

    #Searching an empty tree. The search method handles this by returning false immediately when it detects the
    #absence of a root node.
    emptyTree = BST() #Creation of an empty tree
    print("Searching an empty tree for the number 5:")
    print("Was the value found? :", emptyTree.search(5))

if __name__ == "__main__":
    main()