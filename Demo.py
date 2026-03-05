# ===============================
# Example Program Using Array (List)
# Python Beginner Friendly Code
# ===============================

# Create an array (list) of numbers
numbers = [10, 20, 30, 40, 50]

# Print original array
print("Original Array:")
print(numbers)

# ===============================
# Add new element inside array
# append() is used to add element at the end of list
# ===============================
numbers.append(60)
numbers.append(70)

print("\nArray after adding elements:")
print(numbers)

# ===============================
# Access array elements using index
# Index starts at 0 in Python
# ===============================
print("\nAccessing array elements:")
print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Third element:", numbers[2])

# ===============================
# Modify array element
# Change value at index 1
# ===============================
numbers[1] = 25

print("\nArray after modification:")
print(numbers)

# ===============================
# Remove element from array
# remove() deletes specific value
# ===============================
numbers.remove(40)

print("\nArray after removing 40:")
print(numbers)

# ===============================
# Loop through array
# ===============================
print("\nLooping through array elements:")

for num in numbers:
    print("Value:", num)

# ===============================
# Array length
# len() is used to check number of elements
# ===============================
print("\nTotal number of elements in array:")
print(len(numbers))