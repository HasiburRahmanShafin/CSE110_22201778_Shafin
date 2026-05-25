# LAB-8: Sorting Algorithms (Partial)

# Task 1: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
bubble_sort(my_list)

# Task 2: Selection Sort (stub - to be completed)
def selection_sort(arr):
    # Implementation left as exercise
    pass
