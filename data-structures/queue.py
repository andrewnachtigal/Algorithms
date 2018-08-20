"""
Queue Abstract Data Type

A queue is an ordered collection of items where the addition of new items
happens at one end, called the "rear," and the removal of existing items
occurs at the other end, called the "front."

A queue is ordered as first-in, first-out (FIFO)

Queue Operations:

Queue() creates a new queue that is empty.
enqueue(items) adds a new item to the rear of the queue.
dequeue() removes the front itme from the queue.
isEmpty() tests to see whether the queue is empty
size() returns the number of items in the queue.

Acknowledgments: Introduction to Data Structures and Algorithms in Python

"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# create Queue object and test
q=Queue()
q.size()
q.isEmpty()
