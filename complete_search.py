import random
import time


def create_arrays():
    arr1 = [random.randint(0, 10*N) for i in range(N)]
    arr2 = arr1[:int(N/2)]
    new_numbers = [random.randint(0, 10*N) for i in range(int(N/2))]
    arr2 = arr2 + new_numbers
    return arr1, arr2


def common_lin(arr1, arr2):
    c = 0
    for i in range(len(arr1)):
        key = arr1[i]
        for j in range(len(arr2)):
            if key == arr2[j]:
                c = c + 1
    return c


def main():
    arr1, arr2 = create_arrays()
    c = common_lin(arr1, arr2)
    print("The common numbers between the two are", c)


if __name__ == '__main__':
    N = 1000 #Please use an even integer for N
    random.seed(1046970)
    start = time.time()
    main()
    end = time.time()
    print(end - start)