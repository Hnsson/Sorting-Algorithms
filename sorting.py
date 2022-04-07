from ctypes import sizeof
import sys, time

sys.setrecursionlimit(100000)

# i = parent, k = child, d = d-ary heap
def returnChild(lst: list[int], i, k, d: int = 2):
    # listan, i för föräldern, k villket varn, d är hur många möjliga barn

    # return int(lst[(d*i) + k])
    return int((d*i) + k)

def leftChild(lst: list[int], i):
    return int(2*i + 1)

def leftChild(lst: list[int], i):
    return int(2*i + 2)

def swap(lst: list[int], i, k):
    lst[i], lst[k] = lst[k], lst[i]











def heapsort(lst: list[int], d:	int	= 2):
    # Steg 1 - Konvertera till max-heap
    convertToMaxheap(lst, d)

    # Steg 2 - Iterativt minska mängden och konvertera till max-heap


    return 3

test_1 = [2, 10, 4, 6, 9, 11, 69]

def convertToMaxheap(lst: list[int], d):
    #Last non-leaf node:

    sortedArray = []
    lastNode = int((len(lst) - 2) / d)
    # Nedanför funkar som dem ska
    # print(lastNode)
    # print(lst[lastNode])
    # print(returnChild(lst, lastNode, 2, d))
    # print(lst[returnChild(lst, lastNode, 2, d)])

    # Check last node with children and swap places
    for i in range(lastNode, -1, -1):
        for k in range(1, d + 1):
            # Fungerar men problemet är när en nod har ett barn istället för 2, så måste kolla k bättre
            if(lst[i] < lst[returnChild(lst, i, k, d)]):
                swap(lst, i, returnChild(lst, i, k, d))
    print(lst[0])    
    lst[0] = lst[len(lst) - 1]
    lst.pop()


def quicksort_pivot_first(lst:	list[int]):
    return 2

def quicksort_pivot_median(lst:	list[int]):
    return 1









print("BEFORE -- ", test_1)

convertToMaxheap(test_1, 2)

print("AFTER -- ", test_1)


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




    # for n in range(len(lst)):
    #     for i in range(lastNode, -1, -1):
    #         for k in range(1, d + 1):
    #             if(lst[i] < lst[returnChild(lst, i, k, d)]):
    #                 swap(lst, i, returnChild(lst, i, k, d))
        
    #     sortedArray.append(lst[0])
    #     lst[0] = lst[len(lst) - 1]
    #     lst.pop()
    #     lastNode -= 1
    
    # print(sortedArray)