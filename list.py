# Python program demonstrating list operations

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Print the original list
print("Original list:", numbers)

# Append a new number to the list
numbers.append(6)
print("After appending 6:", numbers)

# Remove a number from the list
numbers.remove(3)
print("After removing 3:", numbers)

# Iterate through the list and print each number
print("Iterating through the list:")
for number in numbers:
    print(number)

# Find the length of the list
length = len(numbers)
print("Length of the list:", length)

# Access a specific element (e.g., the second element, index 1)
second_element = numbers[1]
print("The second element is:", second_element)
