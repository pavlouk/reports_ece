import random
import time


def create_arrays():
    arr1 = [random.randint(0, 10*N) for i in range(N)]
    arr2 = arr1[:int(N/2)]
    new_numbers = [random.randint(0, 10*N) for i in range(int(N/2))]
    arr2 = arr2 + new_numbers
    return arr1, arr2


def binary_s(arr, val):
    if len(arr) == 0 or (len(arr) == 1 and arr[0] != val):
        return 0
    mid = arr[len(arr)//2]
    if val == mid:
        c = 1
        ind = len(arr)//2
        forward = ind + 1
        if forward < len(arr):
            while arr[forward] == val:
                c += 1
                forward += 1
                if forward == len(arr):
                    break
        backward = ind - 1
        if backward > -1:
            while arr[backward] == val:
                c += 1
                backward -= 1
                if backward == -1:
                    break
        return c
    if val < mid:
        return binary_s(arr[:len(arr)//2], val)
    if val > mid:
        return binary_s(arr[len(arr)//2 + 1:], val)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def q_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        q_sort(arr, low, p - 1)
        q_sort(arr, p + 1, high)


def main():
    arr1, arr2 = create_arrays()
    q_sort(arr2, 0, N - 1)
    c = 0
    for i in arr1:
        c = c + binary_s(arr2, i)
    print("The common numbers between the two are", c)


if __name__ == '__main__':
    N = 1000  # Please use an even integer for N
    random.seed(1046970)
    start = time.time()
    main()
    end = time.time()
    print(end - start)
