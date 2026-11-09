# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Purpose

A Binary Search Tree is constructed which is capable of recursive searches, insertion of values, and 
ordering of the values. Each of these methods includes a wrapper method to provide encapsulation, and 
the project is approached through the creation of Node and BST classes.

## Features

1. A Binary Search Tree data structure.
2. Insertion of multiple values.
3. In-order traversal.
4. Test searching.
5. Demonstration of edge cases.
6. A real-world BST example, consisting of guest numbers.

## Reflection

1. ===Concepts and Skills===
The primary skill earned in this assignment was the translation of Binary Search Tree concepts into appropriate
methods. I had taken very detailed notes on the BST operations during class, and the real challenge in this
assignment was building the proper code to execute it. One additional concept I was prepared to encounter but
did not see was the alternate types of traversals of a Binary Search Tree.
2. ===Challenges===
One challenge I encountered was designing the recursive search method. I had initially compared the
wrong values in my checks, resulting in unusual behavior. After carefully tracing
the behavior through the search tree, I realized what had caused the errors and corrected the checks.
3. ===BST Behavior===
A Binary Search Tree is a data structure which organizes nodes according to a greater than and less
than relational rule. This results in a structure which can be more quickly traversed in a search than
similar structures such as linked lists. Each node can have two children, and can itself be a child of
another node. This greatly reduces the time of searches and insertions, because of this implicit encoding
of comparative data in the position of nodes. However, this is not automatically true in all cases: A Binary
Search Tree built in an ascending or descending order can have a highly assymetrical structure which cannot be
quickly traversed for a value. For this reason, it is more efficient to insert values into the BST in a pseudo random
order.