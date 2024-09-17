# WA  program using a loop

# Loop from 1 to 10
for i in range(1, 11):
    print(i)
# Python program demonstrating the use of break and continue

# Loop through numbers from 1 to 20
for i in range(1, 21):
    # Skip the rest of the loop if the number is a multiple of 3
    if i % 3 == 0:
        continue
    
    # Stop the loop completely if the number is 15
    if i == 15:
        break
    
    # Print the current number
    print(i)
