# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/6/22 10:50
# Tool ：PyCharm


def bin_search(data_set, val):
    low = 0
    high = len(data_set)-1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == val:
            print(mid)
            return mid
        elif data_set[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# data = list(range(55))
data = [1, 3, 5, 6, 7, 8, 23, 34, 55]
bin_search(data, 55)
