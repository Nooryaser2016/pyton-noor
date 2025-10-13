def find_length(arr):
# Base case: if the list is empty
    if arr == []:
        return 0
    else:
# Remove first element and call function again
    return 1 + find_length(arr[1:])

# Example list
numbers = [1, 2, 3, 294, 746, 8, 403]

# Print result
print("Length of array:", find_length(numbers))