# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# 1 4 4
# 2 3 4
import itertools

product_list = []
for elem in list(itertools.permutations(range(1,10),9)):
        set1_1, set1_2, set1_3 = elem[0], elem[1]*1000+elem[2]*100+elem[3]*10+elem[4], elem[5]*1000+elem[6]*100+elem[7]*10+elem[8]
        set2_1, set2_2, set2_3 = elem[0]*10+elem[1], elem[2]*100+elem[3]*10+elem[4], elem[5]*1000+elem[6]*100+elem[7]*10+elem[8]
        if set1_1 * set1_2 == set1_3:
            print set1_1, set1_2, set1_3
            product_list.append(set1_3)
        if set2_1 * set2_2 == set2_3:
            print set2_1, set2_2, set2_3
            product_list.append(set2_3)
# print product_list
print sum(list(set(product_list)))
# a = '123456789'
# print a[0], a[0:3], a[3:5]
# print list(itertools.combinations(range(1,10),9))[0]

# print list(itertools.combinations(range(1,4),2))

# 12 483 5796
# 18 297 5346
# 27 198 5346
# 28 157 4396
# 39 186 7254
# 4 1738 6952
# 4 1963 7852
# 42 138 5796
# 48 159 7632
# 45228
# [Finished in 0.9s]