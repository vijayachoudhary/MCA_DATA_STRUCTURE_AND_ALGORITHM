#A program to perform enqueue and dequeue operations on a queue.

def enqueue(queue, item):
    queue.append(item)
    print(f"Enqueued: {item}")

def dequeue(queue):
    queue.pop(0)
    print("Dequeued an item")

queue = [10,20,30]

print("Current queue:", queue)
dequeue(queue)

print("Current queue after dequeue:", queue)

