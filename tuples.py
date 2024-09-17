# Python program using tuple operations

# Create a tuple
fruits = ("apple", "banana", "cherry", "date")

# Print the original tuple
print("Original tuple:", fruits)

# Access elements by index
print("First element:", fruits[0])
print("Third element:", fruits[2])

# Slicing a tuple
sliced_fruits = fruits[1:3]
print("Sliced tuple (from index 1 to 2):", sliced_fruits)

# Tuple concatenation
more_fruits = ("elderberry", "fig")
all_fruits = fruits + more_fruits
print("Concatenated tuple:", all_fruits)

# Tuple repetition
repeated_fruits = fruits * 2
print("Repeated tuple:", repeated_fruits)

# Check if an item exists in the tuple
item_to_check = "banana"
if item_to_check in fruits:
    print(f"{item_to_check} is in the tuple")

# Find the index of an element
index_of_cherry = fruits.index("cherry")
print("Index of 'cherry':", index_of_cherry)

# Count occurrences of an element
count_of_apple = fruits.count("apple")
print("Count of 'apple':", count_of_apple)

# Length of the tuple
length_of_fruits = len(fruits)
print("Length of the tuple:", length_of_fruits)

# Convert a tuple to a list (since tuples are immutable)
fruits_list = list(fruits)
print("Converted to list:", fruits_list)

# Convert a list back to a tuple
fruits_tuple = tuple(fruits_list)
print("Converted back to tuple:", fruits_tuple)


