import time
import random

# ---------------- Sorting Algorithms ---------------- #

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# ---------------- Time Measurement Function ---------------- #

def measure_time(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start


# ---------------- Main Program ---------------- #

size = int(input("Enter number of elements: "))

original = [random.randint(1, 1000) for _ in range(size)]

arr1 = original.copy()
arr2 = original.copy()
arr3 = original.copy()
arr4 = original.copy()

print("\nComparing Sorting Algorithms...\n")

print("Bubble Sort Time   :", measure_time(bubble_sort, arr1))
print("Selection Sort Time:", measure_time(selection_sort, arr2))
print("Insertion Sort Time:", measure_time(insertion_sort, arr3))
print("Merge Sort Time    :", measure_time(merge_sort, arr4))