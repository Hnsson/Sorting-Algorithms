from ctypes import sizeof
import sys, time

sys.setrecursionlimit(100000)

# i = parent, k = child, d = d-ary heap

def heapsort(lst: list[int], d:	int	= 2):
    # Steg 1 - Konvertera till max-heap
    convertToMaxheap(lst, d)

    # Steg 2 - Iterativt minska mängden och konvertera till max-heap


    return 3

test_1 = [2, 10, 69, 6, 9, 11, 4]

def convertToMaxheap(lst: list[int], d):
    #Last non-leaf node:
    lastNode = len(lst) - 2 / d

    # Check last node with children and swap places

    for k in range(1, d + 1):
        if(lst[lastNode] < lst[returnChild(lst, lst[lastNode], k, d)]):
            swap(lst, lastNode, returnChild(lst, lst[lastNode], k, d))

print(test_1)

convertToMaxheap(test_1, 2)

print(test_1)

def returnChild(lst: list[int], i, k, d: int = 2):
    return (d*i) + k

def leftChild(lst: list[int], i):
    return lst[2*i + 1]

def leftChild(lst: list[int], i):
    return lst[2*i + 2]

def swap(lst: list[int], i, k):
    lst[i], lst[k] = lst[k], lst[i]

def quicksort_pivot_first(lst:	list[int]):
    return 2

def quicksort_pivot_median(lst:	list[int]):
    return 1



# Test timer
n = 3000

# Skriv timern runt det du vill ta tid av
# start = time.perf_counter()

# heapsort(n)

# end = time.perf_counter()
# print(end - start)


# f = open("Testdata/1000(0,100000).txt", "r")

# nums = []
# for line in f.readlines():
#     nums.append(int(line.rstrip()))

# print(nums)