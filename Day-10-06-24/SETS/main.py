# Sets in Python

# A set is an unordered collection of unique elements. This means that a set cannot contain duplicate values, and the order of elements in a set is undefined.
# Sets are useful for membership testing, removing duplicates from a sequence, and performing mathematical operations like union, intersection, and difference.

# Creating Sets
# You can create a set using either curly braces {} or the set() constructor.

# Using curly braces
my_set = {1, 2, 3, 4, 5}
print("Set created using '{}' curly brackets:", my_set)  # Output: {1, 2, 3, 4, 5}

# Using set() constructor
another_set = set([4, 5, 6, 7, 8])
print("Set created using set constructor:", another_set)  # Output: {4, 5, 6, 7, 8}

# Set Operations
# Sets support several fundamental operations that are essential for set manipulation and analysis.

# Union (|): Combines all unique elements from two sets into a new set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection (&): Finds elements that are common to both sets.
intersection_set = set1 & set2
print("Intersection:", intersection_set)  # Output: {3}

# Difference (-): Subtracts elements of one set from another.
difference_set = set1 - set2
print("Difference:", difference_set)  # Output: {1, 2}

# Symmetric Difference (^): Generates a new set containing elements that are exclusive to each set.
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Set Methods
# Sets come with a variety of methods for more advanced manipulation.

# add(element): Adds the specified element to the set if it is not already present.
my_set = {1, 2, 3}
print("Before add():", my_set)
my_set.add(4)
print("After add():", my_set)  # Output: {1, 2, 3, 4}

# remove(element): Removes the specified element from the set. Raises a KeyError if the element is not present.
my_set = {1, 2, 3}
print("Before remove():", my_set)
my_set.remove(2)
print("After remove():", my_set)  # Output: {1, 3}

# discard(element): Removes the specified element from the set if it exists. Does not raise an error if the element is not found.
my_set = {1, 2, 3}
print("Before discard():", my_set)
my_set.discard(2)
print("After discard():", my_set)  # Output: {1, 3}

# pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
my_set = {1, 2, 3}
print("Before pop():", my_set)
removed_element = my_set.pop()
print("After pop():", removed_element)  # Output: 1 (or any other element)

# clear(): Removes all elements from the set, making it an empty set.
my_set = {1, 2, 3}
print("Before clear():", my_set)
my_set.clear()
print("After clear():", my_set)  # Output: set()

# copy(): Returns a shallow copy of the set.
my_set = {1, 2, 3}
print("Before copy():", my_set)
copied_set = my_set.copy()
print("After copy():", copied_set)  # Output: {1, 2, 3}

# update(iterable): Adds elements from the specified iterable to the set.
my_set = {1, 2, 3}
print("Before update():", my_set)
my_set.update([4, 5])
print("After update():", my_set)  # Output: {1, 2, 3, 4, 5}

# issubset(other_set): Checks if all elements of the set are present in the specified set.
set1 = {1, 2}
set2 = {1, 2, 3, 4}
result = set1.issubset(set2)
print(result)  # Output: True

# issuperset(other_set): Checks if the set contains all elements of the specified set.
set1 = {1, 2, 3, 4}
set2 = {1, 2}
result = set1.issuperset(set2)
print(result)  # Output: True

# isdisjoint(other_set): Checks if the set has no elements in common with the specified set.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(result)  # Output: True

# Checking Membership with the 'in' Keyword
# You can check if an element is present in a set using the in keyword.
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True
print(6 in my_set)  # Output: False

# Set Comprehension
# Set comprehension is a concise and elegant way to create sets in Python.
squares = {x * x for x in range(1, 6)}
print(squares)  # Output: {1, 4, 9, 16, 25}

# Set comprehension can also include a conditional expression to filter elements.
even_squares = {x * x for x in range(1, 6) if x % 2 == 0}
print(even_squares)  # Output: {4, 16}

# Advanced Set Operations

# Cartesian Product: The set of all ordered pairs (a, b) where 'a' is in set A and 'b' is in set B.
set1 = {1, 2}
set2 = {'a', 'b', 'c'}
cartesian_product = {(x, y) for x in set1 for y in set2}
print(cartesian_product)  # Output: {(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')}

# Power Set: The set of all subsets of a set, including the empty set and the set itself.
def power_set(s):
    if len(s) == 0:
        return {frozenset()}
    element = s.pop()
    subsets = power_set(s)
    return subsets.union({subset.union({element}) for subset in subsets})

my_set = {1, 2, 3}
print(power_set(my_set))  # Output: {frozenset(), frozenset({1}), frozenset({2}), frozenset({3}), frozenset({1, 2}), frozenset({1, 3}), frozenset({2, 3}), frozenset({1, 2, 3})}

# Frozen Set: An immutable version of a set.
my_set = {1, 2, 3}
frozen_set = frozenset(my_set)
print(frozen_set)  # Output: frozenset({1, 2, 3})

# Practical Examples and Use Cases

# 1. Removing Duplicate Elements
duplicate_list = ['apple', 'banana', 'apple', 'orange']
unique_list = list(set(duplicate_list))
print(unique_list)  # Output: ['apple', 'banana', 'orange']

# 2. Finding Common Elements
set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'cherry', 'date'}
common_elements = set1 & set2
print(common_elements)  # Output: {'banana', 'cherry'}

# 3. Counting Unique Elements
elements = ['apple', 'banana', 'apple', 'orange']
unique_counts = {element: elements.count(element) for element in set(elements)}
print(unique_counts)  # Output: {'apple': 2, 'banana': 1, 'orange': 1}

# 4. Filtering Data
data = [1, 2, 3, 4, 5, 6]
filtered_data = {x for x in data if x % 2 == 0}
print(filtered_data)  # Output: {2, 4, 6}