import math
import random

# print(math.log(256, 2))

arr = [i for i in range(1651)]
rand_arr = [random.randint(1, 10) for i in range(20)]
# Бинарный поиск


class Bin_search:
    def __init__(self, arr):
        self.arr = arr

    def get_num(self, num):
        low = 0
        high = len(self.arr)

        while True:
            mid = (low + high) // 2
            if num < mid:
                high = mid - 1
            elif num > mid:
                low = mid + 1
            else:
                return mid

# print(Bin_search(arr).get_num(1649))


# selection sort
def selsort(arr):
    for i, e in enumerate(arr):

        minn = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[minn] = arr[minn], e
        print(arr)
    return arr

# print(selsort([3, 7, 6, 5, 3]))


def recurs(a):
    recurs.__setattr__('a', 0)
    if a < -2:
        recurs(a + 1)
    if recurs.__getattribute__('a') == 10:
        ret
    print(a)
    recurs.__setattr__('a', recurs.a + 1)
    recurs(a - 1)


recurs(2)
