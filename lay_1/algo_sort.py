import math
import random

# print(math.log(256, 2))

arr = [i for i in range(30)]
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

# рекурсия


def recurs_count(a):
    if a == 0:  # базовый случай
        return

    print(a)  # рабочая часть функции
    recurs_count(a - 1)  # самовызов функции

# recurs_count(12)


def sum_arr(arr, n):
    print(arr)
    if len(arr) < 2:
        return 'no answer'

    res_index = len(arr) // 2
    if arr[res_index] == n:
        return arr[res_index]
    else:
        if arr[res_index] > n:
            arr = arr[0:res_index]
            return sum_arr(arr, n)
        else:

            return sum_arr(arr[res_index:], n)


print(sum_arr(sorted(rand_arr), n=int(input())))
print('ready')