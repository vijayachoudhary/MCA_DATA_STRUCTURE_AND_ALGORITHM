#One-dimensional array

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

print("Array elements are:")
for i in range(len(arr)):
    print("Index",i,"=",arr[i])