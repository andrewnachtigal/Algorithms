"""
Binary Search

Given a sorted array arr[] of n elements, write  function to search a given
element x in arr[].

Binary Search: Search a sorted array by repeatedly dividing the search interval
in half. Begin with an interval covering the whole array. If the value of the
search key is less than the item in the middle of the interval, narrow the
interval to the lower half. Otherwise narrow it to the upper half.

Repeatedly check until the value is found or the interval is empty.


"""

def binarySearch(alist, item):
    first = 0
    last = len(alist) -1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

testlist = [0,1,2,8,17, 40]
print(binarySearch(testlist, 2))
print(binarySearch(testlist, 13))
