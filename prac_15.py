def merge_sort(arr):
    if len(arr) > 1:

        # Find the middle index
        mid = len(arr) // 2

        # Divide the array into two halves
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements of left half
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements of right half
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Main Program
arr = [38, 27, 43, 3, 9, 82, 10]

print("Original Array:", arr)

merge_sort(arr)

print("Sorted Array:", arr)