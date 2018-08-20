"""
Deque Abstract Data Type

the deque is structured as an ordered collection of itmes where items are added
and removed from either end, either front or rear.

Deque() creates a new deque that is empty.
addFront(item) adds a new item to the front of the deque.
addRear(item) adds a new item to the rear of the deque.
removeFront() removes the front item from the deque.
removeRear() removes the rear item from the deque
isEmpty() tests to see whether the deque is empty.
size() returns the number of items in the deque.



Acknowledgements: Problems with Algorithms and Data Structures
"""

# Listing 1 - rear of deque is at postion 0 in a Python list.

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# test

d = Deque()
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
print(d.removeFront())
