# Once upon a time, in the land of Python, there were two special collections called Tuples and Lists.
# They were used to store multiple items in a single variable.

# Tuples were like magical boxes that could hold many items, but once you put something in, you couldn't change it.
# Lists, on the other hand, were like flexible bags that you could add to, remove from, and change items inside.

# Let's start our story with Tuples.

# Chapter 1: The Unchangeable Tuple
# Tuples are written with round brackets.

# 1. Meet the fruit tuple
fruit_tuple = ("apple", "banana", "cherry")
print(fruit_tuple)  # Output: ('apple', 'banana', 'cherry')

# 2. Tuples can have duplicate items
duplicate_fruit_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(duplicate_fruit_tuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')

# 3. Tuples have a fixed length
fixed_length_tuple = tuple(("apple", "banana", "cherry"))
print(len(fixed_length_tuple))  # Output: 3

# 4. Tuples can store different types of items
mixed_type_tuple = ("abc", 34, True, 40, "male")
print(mixed_type_tuple)  # Output: ('abc', 34, True, 40, 'male')

# 5. You can also create a tuple using the tuple() constructor
constructed_tuple = tuple(("apple", "banana", "cherry"))
print(constructed_tuple)  # Output: ('apple', 'banana', 'cherry')

# 6. Accessing items in a tuple
access_tuple = ("apple", "banana", "cherry")
print(access_tuple[1])  # Output: 'banana'

# 7. Slicing a tuple
slice_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(slice_tuple[2:5])  # Output: ('cherry', 'orange', 'kiwi')

# 8. Slicing from the beginning to a specific index
beginning_slice_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(beginning_slice_tuple[:4])  # Output: ('apple', 'banana', 'cherry', 'orange')

# 9. Slicing with negative indices
negative_slice_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(negative_slice_tuple[-4:-1])  # Output: ('orange', 'kiwi', 'melon')

# 10. Converting a tuple to a list to modify it
modifiable_tuple = ("apple", "banana", "cherry")
modifiable_list = list(modifiable_tuple)
modifiable_list.append("orange")
modifiable_tuple = tuple(modifiable_list)
print(modifiable_tuple)  # Output: ('apple', 'banana', 'cherry', 'orange')

# 11. Deleting a tuple
deletable_tuple = ("apple", "banana", "cherry")
del deletable_tuple
# print(deletable_tuple)  # This will raise an error because the tuple no longer exists

# 12. Using Asterisk* to unpack tuples
unpack_tuple = ("apple", "mango", "papaya", "pineapple", "cherry")
(first_fruit, *middle_fruits, last_fruit) = unpack_tuple
print(first_fruit)  # Output: 'apple'
print(middle_fruits)  # Output: ['mango', 'papaya', 'pineapple']
print(last_fruit)  # Output: 'cherry'

# 13. Looping through a tuple
loop_tuple = ("apple", "banana", "cherry")
for fruit in loop_tuple:
    print(fruit)  # Output: 'apple' 'banana' 'cherry'

# 14. Creating a tuple with repeated elements
repeat_number = 5  # Number to repeat
repeat_count = 3  # Number of repetitions
repeated_elements_tuple = tuple(range(repeat_number)) * repeat_count
print("Tuple with repeated elements:", repeated_elements_tuple)  # Output: (0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4)

# 15. Looping through a tuple with a while loop
while_loop_tuple = ("apple", "banana", "cherry")
index = 0
while index < len(while_loop_tuple):
    print(while_loop_tuple[index])  # Output: 'apple' 'banana' 'cherry'
    index += 1

# 16. Joining two tuples
first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
joined_tuple = first_tuple + second_tuple
print("Joined tuple:", joined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# 17. Multiplying a tuple
multiply_tuple = ("apple", "banana", "cherry")
multiplied_tuple = multiply_tuple * 2
print(multiplied_tuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Chapter 2: The Count and Index Methods
# Tuples have special methods to count occurrences and find the index of items.

# 1. Counting occurrences in a tuple
count_tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
count_tuple2 = ('python', 'geek', 'python', 'for', 'java', 'python')
count_3 = count_tuple1.count(3)
print('Count of 3 in count_tuple1 is:', count_3)  # Output: 3
count_python = count_tuple2.count('python')
print('Count of Python in count_tuple2 is:', count_python)  # Output: 3

# 2. Counting occurrences of nested items
nested_tuple = (0, 1, (2, 3), (2, 3), 1, [3, 2], 'geeks', (0,))
count_nested_tuple = nested_tuple.count((2, 3))
print('Count of (2, 3) in nested_tuple is:', count_nested_tuple)  # Output: 2
count_list_in_tuple = nested_tuple.count([3, 2])
print('Count of [3, 2] in nested_tuple is:', count_list_in_tuple)  # Output: 1

# 3. Counting specific items
specific_fruits_tuple = ("apple", "banana", "orange", "apple", "grape")
apple_count = specific_fruits_tuple.count("apple")
print("Number of apples:", apple_count)  # Output: 2

# 4. Counting numbers
numbers_count_tuple = (1, 2, 3, 2, 1, 4)
count_1 = numbers_count_tuple.count(1)
count_2 = numbers_count_tuple.count(2)
print("Count of 1:", count_1)  # Output: 2
print("Count of 2:", count_2)  # Output: 2

# 5. Finding the index of items in a tuple
index_tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
first_index_3 = index_tuple.index(3)
print('First occurrence of 3 is', first_index_3)  # Output: 3
first_index_3_after_4 = index_tuple.index(3, 4)
print('First occurrence of 3 after 4th index is:', first_index_3_after_4)  # Output: 7

# 6. Handling errors when the item is not found
try:
    index_not_found = index_tuple.index(4)
except ValueError:
    print("Element not found in the tuple")  # Output: Element not found in the tuple

# 7. Finding the index of items in a tuple with a range
range_fruits_tuple = ("apple", "banana", "cherry", "banana")
index_of_banana = range_fruits_tuple.index("banana")
print(index_of_banana)  # Output: 1
try:
    index_of_mango = range_fruits_tuple.index("mango")
except ValueError:
    print("Element 'mango' not found in the tuple")  # Output: Element 'mango' not found in the tuple

# 8. Finding the index of items in a tuple with a specified range
range_numbers_tuple = (10, 20, 30, 40, 20)
index_after_first_20 = range_numbers_tuple.index(20, 1)
print(index_after_first_20)  # Output: 4
index_in_specified_range = range_numbers_tuple.index(20, 2, 4)
print(index_in_specified_range)  # Output: 4

# Chapter 3: Built-in Functions for Lists and Tuples
# Python has some magical built-in functions that work with both lists and tuples.

# 1. Finding the length of a list or tuple
length_list = [1, 2, 3, 4, 5]
length_of_list = len(length_list)
print("Length of the list:", length_of_list)  # Output: 5
length_tuple = (10, 20, 30)
length_of_tuple = len(length_tuple)
print("Length of the tuple:", length_of_tuple)  # Output: 3

# 2. Calculating the sum of elements in a list or tuple
sum_list = [1, 2, 3, 4, 5]
total_sum_list = sum(sum_list)
print("Sum of numbers:", total_sum_list)  # Output: 15
sum_tuple = (10, 20, 30)
total_sum_tuple = sum(sum_tuple)
print("Sum of numbers_tuple:", total_sum_tuple)  # Output: 60

# 3. Finding the largest element in a list or tuple
largest_list = [1, 5, 2, 8, 3]
largest_number_list = max(largest_list)
print("Largest number:", largest_number_list)  # Output: 8
largest_tuple = (10, 20, 30)
largest_number_tuple = max(largest_tuple)
print("Largest number in tuple:", largest_number_tuple)  # Output: 30

# 4. Finding the smallest element in a list or tuple
smallest_list = [1, 5, 2, 8, 3]
smallest_number_list = min(smallest_list)
print("Smallest number:", smallest_number_list)  # Output: 1
smallest_tuple = (10, 20, 30)
smallest_number_tuple = min(smallest_tuple)
print("Smallest number in tuple:", smallest_number_tuple)  # Output: 10

# 5. Sorting a list or tuple
unsorted_list = [1, 5, 2, 8, 3]
sorted_list = sorted(unsorted_list)
print("Sorted list:", sorted_list)  # Output: [1, 2, 3, 5, 8]
unsorted_tuple = (10, 20, 30, 4, 5)
sorted_tuple = sorted(unsorted_tuple)
print("Sorted tuple:", sorted_tuple)  # Output: [4, 5, 10, 20, 30]

# Chapter 4: Hands-on Exercises
# Let's practice what we've learned with some exercises.

# Q1. Accessing individual elements
fruit_list = ["apple", "banana", "cherry"]
first_fruit = fruit_list[0]  # Accesses "apple"
last_fruit = fruit_list[-1]  # Accesses "cherry" (negative indexing starts from the end)

# Q2. Extracting a sublist
number_list = [1, 2, 3, 4, 5]
sublist1 = number_list[1:4]  # Extracts [2, 3, 4] (includes index 1, excludes 4)
sublist2 = number_list[2:]  # Extracts [3, 4, 5] (from index 2 to the end)

# Q3. Copying a list
original_number_list = [6, 7, 8]
copied_list = original_number_list[:]  # Creates a shallow copy

# Q4. Reversing a list
letter_list = ['a', 'b', 'c', 'd']
reversed_letter_list = letter_list[::-1]  # Extracts [d, c, b, a]

# Q5. Counting occurrences in a string
message_string = "Hello, world! How is your day?"
count_of_o = message_string.count('o')  # Case-sensitive counting
print(count_of_o)  # Output: 2

# Q6. Counting the occurrences of 2
number_count_list = [1, 2, 2, 3, 1, 4, 2]
count_of_2 = number_count_list.count(2)
print(count_of_2)  # Output: 3

# Q7. Finding the length of a list or tuple
length_number_list = [1, 2, 3, 4, 5]
length_number_tuple = (6, 7, 8, 9)
list_length = len(length_number_list)
tuple_length = len(length_number_tuple)
print("Length of list:", list_length)  # Output: 5
print("Length of tuple:", tuple_length)  # Output: 4

# Q8. Finding the smallest element in a list or tuple
fruit_list = ["apple", "banana", "cherry"]
fruit_tuple = ("mango", "kiwi", "grape")
smallest_fruit_list = min(fruit_list)
smallest_fruit_tuple = min(fruit_tuple)
print("Smallest fruit in list:", smallest_fruit_list)  # Output: apple
print("Smallest fruit in tuple:", smallest_fruit_tuple)  # Output: grape

# Q9. Finding the largest element in a list or tuple
largest_number_list = [1, 5, 2, 8]
largest_number_tuple = (3, 7, 9, 0)
largest_number_in_list = max(largest_number_list)
largest_number_in_tuple = max(largest_number_tuple)
print("Largest number in list:", largest_number_in_list)  # Output: 8
print("Largest number in tuple:", largest_number_in_tuple)  # Output: 9

# Q10. Sorting a list
mixed_type_list = ["apple", 3, 9.5, True]
mixed_type_list.sort()  # Sorts the list in-place
print("Sorted list:", mixed_type_list)  # Output: [3, 9.5, True, apple] (depending on Python version)

# Q11. Calculating the sum of elements in a list or tuple
sum_number_list = [4, 7, 2, 11]
sum_number_tuple = (6, 3, 8, 1)
list_sum = sum(sum_number_list)
tuple_sum = sum(sum_number_tuple)
print("Sum of list elements:", list_sum)  # Output: 24
print("Sum of tuple elements:", tuple_sum)  # Output: 18

# And they lived happily ever after in the land of Python, using Tuples and Lists to store their data.