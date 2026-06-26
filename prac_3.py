#Basic operations on list

lst = []

#insertion
lst.append(10)
lst.append(20)
lst.append(30)

print("After insertion:", lst)

#Traversal

print("Traversing list:")
for item in lst:
    print(item, end=" ")

#Searching

key = 20
if key in lst:
    print(f"\nElement {key} found at index: {lst.index(key)}")
else:
    print(f"\nElement {key} not found in the list.")

#Deletion
lst.remove(20)
print("After deletion:", lst)
