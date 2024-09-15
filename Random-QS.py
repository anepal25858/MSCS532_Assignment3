import sys
import time
import random

# Increase the recursion limit since we were getting "RecursionError: maximum recursion depth exceeded" error
sys.setrecursionlimit(1500)

# Randomized Quicksort
def randomizedQS(array):
    if len(array) <= 1:
        return array
    pivot = array[random.randint(0, len(array) - 1)]  # Randomly choosing pivot

    lessThanPivot = []
    equalToPivot = []
    greaterThanPivot = []

    for x in array:
        if x < pivot:
            lessThanPivot.append(x)
        elif x == pivot:
            equalToPivot.append(x)
        else:
            greaterThanPivot.append(x)

    return randomizedQS(lessThanPivot) + equalToPivot + randomizedQS(greaterThanPivot)

# Deterministic Quicksort
def deterministicQS(array):
    stack = [(0, len(array) - 1)]

    while stack:
        start, end = stack.pop()

        if start >= end:
            continue

        pivot = array[start]  # First element as the pivot
        left, right = start + 1, end

        # Partition the array
        while left <= right:
            if array[left] <= pivot:
                left += 1
            elif array[right] > pivot:
                right -= 1
            else:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1


        array[start], array[right] = array[right], array[start]


        stack.append((start, right - 1))  # Left subarray
        stack.append((right + 1, end))  # Right subarray

    return array

# test cases
def testCases(size):
    randomArray = [random.randint(0, size) for _ in range(size)]
    sortedArray = list(range(size))
    reverseArray = list(range(size, 0, -1))
    repeatedArray = [size // 2] * size
    return randomArray, sortedArray, reverseArray, repeatedArray

# measure execution time
def executionTime(array, sorting_func):
    start_time = time.time()
    sorting_func(array.copy())
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":

    #test cases
    arr1 = []
    print("Empty:", randomizedQS(arr1))

    # repeated elements
    arr2 = [3, 1, 2, 1, 5, 3, 2, 4]
    print("Repeated:", randomizedQS(arr2))

    # sorted array
    arr3 = [1, 2, 3, 4, 5]
    print("Sorted:", randomizedQS(arr3))

    # Reverse sorted
    arr4 = [5, 4, 3, 2, 1]
    print("Reverse Sorted:", randomizedQS(arr4))

    #different input size
    input = [100, 1000, 5000, 10000]
    for size in input:
        print(f"\nArray size: {size}")
        randomArray, sortedArray, reverseArray, repeatedArray = testCases(size)

        # Testing Randomized Quicksort
        print("\nRandomized Quicksort:")
        print(f"Random Array: {executionTime(randomArray, randomizedQS):.5f} seconds")
        print(f"Sorted Array: {executionTime(sortedArray, randomizedQS):.5f} seconds")
        print(f"Reverse Sorted Array: {executionTime(reverseArray, randomizedQS):.5f} seconds")
        print(f"Repeated Elements Array: {executionTime(repeatedArray, randomizedQS):.5f} seconds")

        # Testing Deterministic Quicksort
        print("\nDeterministic Quicksort (first element as pivot):")
        print(f"Random Array: {executionTime(randomArray, deterministicQS):.5f} seconds")
        print(f"Sorted Array: {executionTime(sortedArray, deterministicQS):.5f} seconds")
        print(f"Reverse Sorted Array: {executionTime(reverseArray, deterministicQS):.5f} seconds")
        print(f"Repeated Elements Array: {executionTime(repeatedArray, deterministicQS):.5f} seconds")
