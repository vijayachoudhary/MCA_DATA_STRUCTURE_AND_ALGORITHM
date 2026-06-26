def selection_sort(arr,n):
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        swap = arr[i]
        arr[i] = arr[min]
        arr[min] = swap

arr = [64, 25, 12, 22, 11]
n = len(arr)

selection_sort(arr,n)

print("Sorted array:", arr)
