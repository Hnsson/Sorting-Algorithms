""" Implementation of 2 sorting algorithms (quick-sort, heapsort) """
import sys
import time

sys.setrecursionlimit(100000000)

def swap(lst, i, k):
    """ Swap two elements in an array """
    lst[i], lst[k] = lst[k], lst[i]

def heapsort(lst, d = 2):
    """ Main function controlling heapsort """
    convert_to_maxheap(lst, len(lst), d)

    for n in range(len(lst) - 1, 0, -1):
        swap(lst, 0, n)
        max_heapify(lst, 0, n, d)

    return lst

def max_heapify(lst, i, current_length, d):
    """ Max heapify a given node (subtree) """
    largest = lst[i]
    largest_index = i

    for k in range(i*d+1, i*d+d + 1):
        if k < current_length and lst[k] > largest:
            largest = lst[k]
            largest_index = k
    if lst[i] < largest:
        swap(lst, i, largest_index)
        max_heapify(lst, largest_index, current_length, d)

def convert_to_maxheap(lst, current_length, d):
    """ Convert a heap to a max-heap """
    last_node = (current_length - 2) // d

    for i in range(last_node, -1, -1):
        max_heapify(lst, i, current_length, d)

def partition(lst, begin, end):
    """ Calculating partition and pivot point """
    pivot = lst[begin]
    i = begin

    for j in range(begin + 1, end):
        if lst[j] <= pivot:
            i += 1
            swap(lst, i, j)

    swap(lst, begin, i)
    return i

def quicksort_pivot_first(lst):
    """ Main function controlling quicksort for pivot first version """
    quick_sort_first(lst, 0, len(lst))


def quick_sort_first(lst, begin, end):
    """ Quicksort algorithm with pivot first """
    if begin < end:
        pivot = partition(lst, begin, end)
        quick_sort_first(lst, begin, pivot)
        quick_sort_first(lst, pivot + 1, end)
    return lst

def calc_pivot(lst, begin, end):
    """ Calculating pivot point based on median of 3 """
    end_2 = end - 1
    mid = (end - begin)// 2
    pivot = end_2

    if lst[begin] > lst[mid]:
        if lst[begin] < lst[end_2]:
            pivot = begin
        elif lst[mid] > lst[end_2]:
            pivot = mid
        else:
            pivot = end_2
    else:
        if lst[begin] > lst[end_2]:
            pivot = begin
        elif lst[mid] < lst[end_2]:
            pivot = mid
        else:
            pivot = end_2

    return pivot

def partition_median(lst, begin, end):
    """ Calculate partition and pivot point """
    pivot_i = calc_pivot(lst, begin, end)
    pivot = lst[pivot_i]

    lst[pivot_i], lst[begin] = lst[begin], lst[pivot_i]

    i = begin

    for j in range(begin, end):
        if lst[j] < pivot:
            i += 1
            swap(lst, j, i)

    swap(lst, begin, i)
    return i

def quicksort_pivot_median(lst):
    """ Main function controlling quicksort for median version """
    quick_sort_median(lst, 0, len(lst))

    return lst

def quick_sort_median(lst, begin, end):
    """ Quicksort algorithm with median pivot """
    if begin < end:
        pivot = partition_median(lst, begin, end)
        quick_sort_median(lst, begin, pivot)
        quick_sort_median(lst, pivot + 1, end)
    return lst

def is_sorted(lst):
    """ Help function which linearly search list and check if sorted """
    flag = 0
    i = 1
    while i < len(lst):
        if lst[i] < lst[i - 1]:
            flag = 1
        i += 1

    if not flag:
        print("Yes, List is sorted.")
    else:
        print("No, List is not sorted.")


if __name__ == '__main__':
    # TEST CASES
    # f = open("Testdata/1000(0,100000).txt", "r")
    # f = open("Testdata/10000(0,100000).txt", "r")

    nums = []

    with open("Testdata/random_100000.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            nums.append(int(line.rstrip()))

    # -- RUN --
    start_time = time.perf_counter()

    # quicksort_pivot_first(nums)
    # quicksort_pivot_median(nums)
    heapsort(nums, 2)

    end_time = time.perf_counter()

    print("Time for algorithm: ", end_time - start_time)
    is_sorted(nums)
