# Python program demonstrating dictionary operations

# Create a dictionary
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

# Print the original dictionary
print("Original dictionary:", student_scores)

# Access a value by key
print("Score of Alice:", student_scores["Alice"])

# Add a new key-value pair
student_scores["Eve"] = 88
print("After adding Eve:", student_scores)

# Update the value for an existing key
student_scores["Bob"] = 95
print("After updating Bob's score:", student_scores)

# Remove a key-value pair
del student_scores["Charlie"]
print("After removing Charlie:", student_scores)

# Check if a key exists in the dictionary
key_to_check = "David"
if key_to_check in student_scores:
    print(f"{key_to_check} is in the dictionary with score {student_scores[key_to_check]}")

# Get a value using the get() method (with default value)
score_of_eve = student_scores.get("Eve", "Not found")
print("Score of Eve (using get()):", score_of_eve)

# Get all keys from the dictionary
keys = student_scores.keys()
print("Keys in the dictionary:", list(keys))

# Get all values from the dictionary
values = student_scores.values()
print("Values in the dictionary:", list(values))

# Get all key-value pairs from the dictionary
items = student_scores.items()
print("Key-value pairs in the dictionary:", list(items))

# Find the number of items in the dictionary
num_items = len(student_scores)
print("Number of items in the dictionary:", num_items)

# Clear all items in the dictionary
student_scores.clear()
print("After clearing all items:", student_scores)
