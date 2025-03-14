import time
import random
import matplotlib.pyplot as plt
import numpy as np

# 📌 Bubble Sort Implementation (To be completed by students)
def bubble_sort(arr):
    length = len(arr)

    for p in range(length - 1):
        swapped = False

        for i in range(length - 1 - p):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

    return arr


# 📌 Selection Sort Implementation (To be completed by students)
def selection_sort(arr):
    length = len(arr)

    for p in range(length - 1):
        k = p

        for i in range(p + 1, length):
            if arr[i] < arr[k]:
                k = i
        arr[p], arr[k] = arr[k], arr[p]

    return arr

# 📌 Insertion Sort Implementation (To be completed by students)
def insertion_sort(arr):
    length = len(arr)
    for i in range(1,length):
        Key=arr[i]
        j=i-1
        while j >= 0 and arr[j] > Key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = Key

    return arr

# 📌 Function to test sorting performance
def test_sorting_performance():
    """
    Generates lists of random numbers and tests the execution time of sorting algorithms.
    """
    # Create arrays of different sizes
    sizes = [1000 * i for i in range(0, 11)]  # From 1000 to 10000 with step 1000
    dataset = []

    for size in sizes:
        dataset.append([random.uniform(1, 100) for _ in range(size)])

    # Create data for timing results
    times1 = []  # Bubble sort
    times2 = []  # Selection sort
    times3 = []  # Insertion sort
    times4 = []  # Python's built-in sort

    # Measure execution times
    for data in dataset:
        # Make copies to avoid sorting already sorted arrays
        data1 = data.copy()
        data2 = data.copy()
        data3 = data.copy()
        data4 = data.copy()

        # Bubble sort
        start = time.time()
        bubble_sort(data1)
        end = time.time()
        times1.append(end - start)

        # Selection sort
        start = time.time()
        selection_sort(data2)
        end = time.time()
        times2.append(end - start)

        # Insertion sort
        start = time.time()
        insertion_sort(data3)
        end = time.time()
        times3.append(end - start)

        # Python's built-in sort
        start = time.time()
        sorted(data4)
        end = time.time()
        times4.append(end - start)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times1, 'o-', label='Bubble Sort')
    plt.plot(sizes, times2, 's-', label='Selection Sort')
    plt.plot(sizes, times3, '^-', label='Insertion Sort')
    plt.plot(sizes, times4, 'v-', label='Python Built-in Sort')

    # Add labels and title
    plt.xlabel('Input Size (number of elements)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithm Runtime Comparison')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()





# Run the performance test
test_sorting_performance()







