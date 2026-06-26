#singly linked list using dictionary without classes.

#creating nodes (dictionary)

n1 = {"data": 10, "next": None}
n2 = {"data": 20, "next": None}
n3 = {"data": 30, "next": None}

#linking nodes
n1["next"] = n2
n2["next"] = n3

#head

head = n1

#displaying linked list

temp = head
while temp is not None:
    print(temp["data"], end=" -> ")
    temp = temp["next"]
print("None")

