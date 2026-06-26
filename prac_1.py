#insert and delete element at given position

lst = [10,20,30,40,50]
print("Original list:", lst)

#insert

pos = int(input("Enter position to insert(0-based index): "))
element = int(input("Enter element to insert: "))

if pos >= 0 and pos <= len(lst):
    lst.insert(pos, element)
    print("List after insertion:", lst)

else:
    print("Invalid position for insertion.")

#delete

pos = int(input("Enter position to delete(0-based index): "))

if pos >= 0 and pos < len(lst):
    deleted_element = lst.pop(pos)
    print(f"Deleted element: {deleted_element}")
    print("List after deletion:", lst)
else:
    print("Invalid position for deletion.")

