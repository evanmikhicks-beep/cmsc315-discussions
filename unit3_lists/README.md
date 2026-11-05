

==== Concepts & Skills ====
    The main skill gained from this assignment is the translation of Java list usage to Python.
Although Python is typically simpler to program in due to dynamic typing, I did have to refer back to 
Python documentation to ensure I was using the correct syntax.
    Additionally, this is my largest exposure to a list manipulating program to date. I will certainly learn
more about implementing lists as I continue to work on database structures and algorithms. In this case I
designed the list around a theoretical list of customer names, which relates directly to real world applications
and will likely be a concept utilized in far more complex data structures in the future.

==== Challenges ====
    The largest challenge in implementing the list program was determining the logical flow of deleting an
item from a Python list. I initially tried to jump directly to the .pop method, but this was not appropriate
for the validations that needed to occur first. Additionally, I nearly implemented an incorrect check of the
range for a provided value, by using [ i > len(lst) ] vice [ i >= len(lst) ].

==== Performance ====
    When considering the performance of list operations, it is important to think of the actual steps that
each method will perform on the list. Although often a single item is manipulated, this can cause the entire
list to shift index by one, which can consume resources in very large datasets. Deleting or adding items can
cause all items of a greater index to shift by one, and the worst case performance of a search is O[N], where
each item will be searched and no matching value found.
*Additional edits added for Commit testing on a new device.