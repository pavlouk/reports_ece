import random
import time


class Number:
    def __init__(self, num):
        self.num = num
        self.frequency = 1

    def update(self):
        self.frequency += 1


def create_arrays():
    arr1 = [random.randint(0, 10*N) for i in range(N)]
    arr2 = arr1[:int(N/2)]
    new_numbers = [random.randint(0, 10*N) for i in range(int(N/2))]
    arr2 = arr2 + new_numbers
    return arr1, arr2


def store_hash(number):
    ind = number % prime
    if h_table[ind] == []:
        h_table[ind] = Number(number)
    elif h_table[ind].num == number:
        h_table[ind].update()
    else:
        while h_table[ind].num != number or h_table[ind] == []:
            ind += 1
            if ind == prime:
                ind = 0
            if h_table[ind] == []:
                h_table[ind] = Number(number)
                break
            elif h_table[ind].num == number:
                h_table[ind].update()
                break


def find_comm(number):
    ind = number % prime
    if h_table[ind] == []:
        return 0
    elif h_table[ind].num == number:
        return h_table[ind].frequency
    else:
        while h_table[ind].num != number and h_table[ind] != []:
            ind += 1
            if ind == prime:
                ind = 0
            if h_table[ind].num == number:
                return h_table[ind].frequency


def main():
    arr1, arr2 = create_arrays()
    c = 0
    for i in arr1:
        store_hash(i)
    for i in arr2:
        c += find_comm(i)
    print("The common numbers between the two are", c)


if __name__ == '__main__':
    N = 1000 #Please use an even integer for N
    prime = 20*N
    prime = 20011
    h_table = [[]]*prime
    random.seed(1046970)
    start = time.time()
    main()
    end = time.time()
    print(end - start)