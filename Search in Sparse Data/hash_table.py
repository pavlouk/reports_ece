import random


class Card:
    def __init__(self, card_ID, card_dept):
        self.card_ID = card_ID
        self.dept = card_dept
        self.usages = 1

    def update(self, price):
        self.dept += price
        self.usages += 1


def createSale():
    s = ['1', '2', '3', '4', '5', '6', '7', '8',
         '9', '0', '1', '2', '3', '4', '5', '6']
    s_a = random.randint(0, 15)
    s_b = random.randint(0, 15)
    s_c = random.randint(0, 15)
    s_d = random.randint(0, 15)
    while s_a == s_b or s_a == s_c or s_a == s_d or s_b == s_c or s_b == s_d or s_c == s_d:
        s_a = random.randint(0, 15)
        s_b = random.randint(0, 15)
        s_c = random.randint(0, 15)
        s_d = random.randint(0, 15)
    s[s_a] = 'A'
    s[s_b] = 'B'
    s[s_c] = 'C'
    s[s_d] = 'D'
    customer_ID = "".join(s)
    customer = 0
    for i in range(len(s)):
        customer += ord(s[i])*7**(i)
    price = random.randint(10, 1000)
    return customer, customer_ID, price


def store_hash(customer, customer_ID, price):
    ind = customer % 87383
    if h_table[ind] == []:
        h_table[ind] = Card(customer_ID, price)
    elif h_table[ind].card_ID == customer_ID:
        h_table[ind].update(price)
    else:
        while h_table[ind].card_ID != customer_ID or h_table[ind] == []:
            ind += 1
            if ind == 87383:
                ind = 0
            if h_table[ind] == []:
                h_table[ind] = Card(customer_ID, price)
                break
            elif h_table[ind].card_ID == customer_ID:
                h_table[ind].update(price)
                break


def max_spender_shopper(h_table):
    m = 0
    for i in h_table:
        if i != []:
            if i.dept > m:
                m = i.dept
                max_spender = i
    m = 0
    for i in h_table:
        if i != []:
            if i.usages > m:
                m = i.usages
                max_shopper = i
    print("The customer", max_spender.card_ID,
          "owes the most, with a dept of", max_spender.dept)
    print("The customer", max_shopper.card_ID,
          "shops the most, with usages of", max_shopper.usages)


def main():
    for _ in range(1000000):
        customer, customer_ID, price = createSale()
        store_hash(customer, customer_ID, price)
    max_spender_shopper(h_table)


if __name__ == '__main__':
    h_table = [[]]*87383
    random.seed(1046970)
    main()
