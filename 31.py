# In England the currency is made up of pound, , and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).
# It is possible to make 2 in the following way:

# 11 + 150p + 220p + 15p + 12p + 31p
# How many different ways can 2 be made using any number of coins?

coin_list = [1, 2, 5, 10, 20, 50, 100, 200]

def coin(coin_kind, total_amount):
    if coin_kind == 1:
        return 1
    else:
        count = 0
        while total_amount >=0:
            count += coin(coin_kind-1, total_amount)
            total_amount -= coin_list[coin_kind-1]
        return count


print coin(8, 200)

# 73682
# [Finished in 0.1s]