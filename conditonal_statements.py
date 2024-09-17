# Python program using if, elif, else statements

# Input: age of the person
age = int(input("Enter your age: "))

# Determine the life stage based on age
if age < 0:
    print("Age cannot be negative.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")