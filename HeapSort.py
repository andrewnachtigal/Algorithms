"""
Python Implementation of Heap Sort

Self Study Materials for:
MIT OCW 6.006
Problem Solving with Algorithms and Data Structures

Heap-Sort
Sorting Strategy:                           Complexity
1. Build Max Heap from unorderd array;       O(n)
2. Find maximum element A[1];                O(1)
3. Swap elements A[n] and A[1]:              O(1)
4. Discard node n from heap
        (decrementing heap-size variable)
5. New root may violate max heap property,   O(lgn)
    but its children are max heaps.
    Run max_heapify to fix this.
6. Go to Step 2 unless heap is empty.

Total Complexity for n steps: O(nlgn)

Acknowledgements:
https://www.geeksforgeeks.org/heap-sort/
"""

# To heapify subtree rooted at index i.
# n is size of heap

def heapify(arr, n, i):
    largest = i # initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

    # check if left child of root exists and is grtr than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # check if right child of root exists and is grtr than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # change root, if necessary
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap

        # heapify root
        heapify(arr, n, largest)

    # Main function to sort array of given size
    def heapSort(arr):
        n = len(arr)

        # build a maxheap
        for i in range(n, -1, -1):
            heapify(arr, n, i)

        # Extract elements one by one
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] # swap
            heapify(arr, i, 0)

    # Driver code to test
    arr = [ 12, 11, 13, 5, 6, 7 ]
    heapSort(arr)
    n = len(arr)
    print ( 'Sorted array is' )
    for i in range(n):
        print ('%d' %arr[i] )
