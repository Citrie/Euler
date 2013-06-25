# n^2+an+b

from lib import prime_list, is_prime

a_list = range(-999,1000,2)
b_list = prime_list(1000)

def consecutive_prime(a,b):
    n,length = 0, 0
    while (n*n+a*n+b)>1 and is_prime(n*n+a*n+b):
        n += 1
        length += 1
    return length

a_b_list = []

for a in a_list:
    for b in b_list:
        a_b_list.append([a,b])

len_list = []

for ab in a_b_list:
    len_list.append(consecutive_prime(ab[0],ab[1]))

print max(len_list)
index_len_list = len_list.index(max(len_list))
print index_len_list
print a_b_list[index_len_list]

# 71
# 78955
# [-61, 971]
# [Finished in 1.2s]