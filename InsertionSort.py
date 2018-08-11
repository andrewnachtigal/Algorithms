"""
Python Implementation of Insertion Sort

Self Study Materials for:
MIT OCW 6.006
Problem Solving with Algorithms and Data Structures

"""

def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

# test
alist = [8,37,13,86,2,37,50,7]
insertionSort(alist)
print(alist)
