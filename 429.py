# A unitary divisor d of a number n is a divisor of n that has the property gcd(d, n/d) = 1.
# The unitary divisors of 4! = 24 are 1, 3, 8 and 24.
# The sum of their squares is 12 + 32 + 82 + 242 = 650.

# Let S(n) represent the sum of the squares of the unitary divisors of n. Thus S(4!)=650.

# Find S(100 000 000!) modulo 1 000 000 009.

# which is 149*671141

import math
from lib import *

def process_all_mod(num,modulo_num):
    """actual function"""
    prime_factor_list, prime_factor_power_list = n_factorial_prime_factor_list(num)
    print len(prime_factor_list)
    print prime_factor_list[len(prime_factor_list)]
    modulo_product = 1
    
    for i in range(len(prime_factor_list)):
        ud = 1
        for power in range(prime_factor_power_list[i]):
            ud *= int(prime_factor_list[i])
            ud %= modulo_num
        modulo_product *= ud*ud+1
        modulo_product %= modulo_num
        # if modulo_product == 0: 
        #     print "alert", i, prime_factor_list[i], prime_factor_power_list[i], ud, temp_modulo_product, modulo_product
        #     break
        #     # alert i=3245398 factor=54342623 power=1 ud=54342623 temp=584039149.0 0.0
    return modulo_product, i

# print process_all_mod(100000000,1000000009)
# test
# print process_all_mod(5,110000000000)
# print unitary_divisors(5,10000000)
# print n_factorial_prime_factor_list(5)

# print (54342623*54342623+1)%1000000009
# print find_all_prime_factors(1000000009)
# print find_all_prime_factors(647942050)
# print process_all_mod(8, 23)
# print (584039149.0*(54342623*54342623+1))
# print (584039149*(54342623*54342623+1))
