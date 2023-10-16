import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -i

# In binary search the method used is similar as divide and conquer,
# And we will use a sortef list to execute our metho around it
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1    
    
    # Here we will define the midpoint 
    midpoint = (low + high) // 2
    
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)


if __name__ == '__main__':
    # l = [1, 3, 5, 10, 12, 15, 17, 49]
    # target = 3
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))
    
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Time taken by Naive Search is: ", (end - start)/length, " seconds")
    
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Time taken by Binary Search is: ", (end - start)/length, " seconds")
