# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Purpose

Create methods for both linear and binary searches, compare the efficiency of either on both small and large data sets. Demonstrate edge cases.

## Features

1. Testing both algorithms on a small dataset.
2. Testing both algorithms on a large dataset.
3. Demonstrating edge cases.
4. Real world illustration: Small dataset represents cakewalk numbers.


## Reflection


1. ===Concepts===
The primary concept I learned in this assignment was the difference between implementing linear and binary searches.
While linear searches are a concept that has been thoroughly explored by programming courses up to this point, binary 
searches are an entirely new concept to program myself. They involve logic that extends beyond the simpler logic of a
linear search, to include logic flow based on comparisons of values each time the remaining search space is halved.
2. ===Challenges===
The largest challenge I encountered was not directly related to linear and binary searches. I was attempting to format
the output of my searches and created scope creep in the assignment. Strictly speaking, I was only required to return the
index after each search. I had wanted to add a feature to include the number of values checked per search for richer comparisons
in my output. However, when attempting to implement this I ran into multiple issues. At one point I was returning a formatted string
following each search - but I realized doing so defied the assignment requirements of returning the index of the search. For the sake
of preserving assignment requirements and due to the amount of scope creep I had already introduced, I decided to comment out the logic
I had added and remain satisfied with returning the search index.
3. ===Linear VS Binary Search===
Learning about Binary searching certainly began to open my eyes to how algorithms can greatly increase efficiency.
The Binary Search can greatly reduce the time of a search, because it divides the search space by two during each visit of a value.
In a few cases this will detract from efficient searches (IE a target value is at the beginning of a data structure and would be found 
more quickly by a linear search). Aside from those few cases which are additionally indiscernable with limited knowledge, the binary search
is far more efficient. However, there is a hidden cost of binary searches: They require ordered datasets to function, and this would create
more work to sort data in the real world rather than perform a single linear search. The decision to create sorted data would include consideration
of the reuse of that data and the lifecycle of the program being used.