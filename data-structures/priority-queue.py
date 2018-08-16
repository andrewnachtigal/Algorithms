"""
Problem
Implement a queue that sorts items by a given priority and always returns
the item with the highest priority on each pop operation.

The following class uses the heapq module to implement a simple priority
queue.

Acknowledgements: Python Cookbook
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# use case
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

# test
q = PriorityQueue

q.push(Item('foo'), 1, 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
