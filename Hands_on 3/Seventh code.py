def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2

        # Dividing the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive calls on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements are left in the halves
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Test the Merge Sort with the given array
if __name__ == "__main__":
    array = [5, 2, 4, 7, 1, 3, 2, 6]
    print("Original array:", array)
    merge_sort(array)
    print("Sorted array:", array)
