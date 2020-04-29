import random
import time


def create_arrays():
    arr1 = [random.randint(0, 10*N) for i in range(N)]
    arr2 = arr1[:int(N/2)]
    new_numbers = [random.randint(0, 10*N) for i in range(int(N/2))]
    arr2 = arr2 + new_numbers
    return arr1, arr2


def store_hash(number):
    ind = number % prime
    if h_table[ind] == []:
        h_table[ind] = [number]
    else:
        h_table[ind].append(number)


def find_comm(number):
    ind = number % prime
    if h_table[ind] == []:
        return 0
    else:
        return len(h_table[ind])


def main():
    arr1, arr2 = create_arrays()
    c = 0
    for i in arr1:
        store_hash(i)
    for i in arr2:
        c += find_comm(i)
    print("The common numbers between the two are", c)


if __name__ == '__main__':
    N = 1000  # Please use an even integer for N
    prime = 20*N
    prime = 20011
    h_table = [[]]*prime
    random.seed(1046970)
    start = time.time()
    main()
    end = time.time()
    print(end - start)
