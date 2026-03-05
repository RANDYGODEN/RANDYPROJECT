# ===========================================
# Binary Search Example Using Array (List)
# Explanation is inside the code using comments
# ===========================================

# Sorted array (Binary search requires sorted data)
numbers = [10, 20, 30, 40, 50, 60, 70]

# Value we want to search
target = 40

# Left and right pointer
left = 0
right = len(numbers) - 1

# Flag variable (check if value is found)
found = False

# Loop while search space is valid
while left <= right:

    # Find middle index of array
    # // means integer division (no decimal)
    mid = (left + right) // 2

    # Check if middle value is the target
    if numbers[mid] == target:
        print("Value found at index:", mid)
        found = True
        break  # Stop loop if value is found

    # If target is bigger, search right side
    elif numbers[mid] < target:
        # Move left pointer to mid + 1
        left = mid + 1

    # If target is smaller, search left side
    else:
        # Move right pointer to mid - 1
        right = mid - 1

# If value is not found
if not found:
    print("Value not found in array")