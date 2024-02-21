from queue import PriorityQueue

# Instantiate a priority queue
priority_queue = PriorityQueue()

# Add items to the queue
priority_queue.put((3, 'Hiccups'))
priority_queue.put((1, 'Botulism'))
priority_queue.put((2, 'Rash'))

# Dequeue items and print them
while not priority_queue.empty():
    priority, item = priority_queue.get()  #return tuple
    print(f'Item: {item}, Priority: {priority}')

print(type(priority_queue.get()))
