#a program to perform binary search on a sorted array

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter the target number to search: "))
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found in the array.")


