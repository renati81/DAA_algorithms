#Leverage your implementation of quicksort to implement the ith order statistic. 
#Example outout has provided at the bottom of code.

import random

# QuickSelect function to find the ith order statistic
def quick_select(arr, left, right, k):
    if left == right:  # If the list contains only one element
        return arr[left]

    # Select a random pivot index between left and right
    pivot_index = random.randint(left, right)
    
    # Move the pivot to the end
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    pivot = arr[right]
    
    # Partition the array around the pivot
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    
    # The pivot is now at index i, so check its position
    if i == k:
        return arr[i]
    elif i > k:
        return quick_select(arr, left, i - 1, k)  # Recur on the left of pivot
    else:
        return quick_select(arr, i + 1, right, k)  # Recur on the right of pivot

# Helper function to find the ith order statistic
def find_ith_order_statistic(arr, i):
    if i < 0 or i >= len(arr):
        raise IndexError("Index out of bounds")
    return quick_select(arr, 0, len(arr) - 1, i)

# Example to demonstrate the function
if __name__ == "__main__":
    # Example array
    array = [12, 3, 5, 7, 4, 19, 26]
    i = 3  # Looking for the 4th smallest element (i.e., index 3)
    
    print(f"The {i+1}th smallest element in the array is:", find_ith_order_statistic(array, i))


#Output:
#The 4th smallest element in the array is: 7
