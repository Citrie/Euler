import math

# things about prime numbers

def is_prime(num):
    """check if a number is a prime"""
    for i in range(2,int(math.sqrt(num))+1):
        if not num%i: return False
    return True

def prime_list(n):
    """ Returns  a list of primes < n """
    n+=1
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def n_factorial_prime_factor_list(num):
    """return all the prime factors with their powers of n!
    return as 2 lists, one is all the factors and another is the power"""
    prime_factor_list = prime_list(num)
    prime_factor_power_list = []
    # calculate the power of each prime
    for i in range(len(prime_factor_list)):
        prime = prime_factor_list[i]
        power_sum, power = 0, 1
        while num>=math.pow(prime,power):
            power_sum += int(num/math.pow(prime,power))
            power += 1
        prime_factor_power_list.append(power_sum)
    return prime_factor_list, prime_factor_power_list

# things about factors
def largest_prime_factors(num,factor=2):
    while factor!=num:
        if not num%factor:
            return largest_prime_factors(num/factor,factor)
        factor+=1
    return factor

# def greatest_common_factor(a,b):
#     i = min(a,b)
#     while i:
#         if not a%i and not b%i: return i
#         i-=1

def find_all_factors(num):
    list = []
    for i in range(1,int(math.sqrt(num))+1):
        if not num%i:
            list.append(i)
            if i!= num/i:
                list.append(num/i)
    return list

# def prime_factors_power_list(num, prime_factor_list=[], prime_factor_power_list=[], iter=0):
#     factors = prime_list(int(math.sqrt(num)))
#     length = len(factors)
#     if num ==1:
#         return prime_factor_list, prime_factor_power_list
#     elif is_prime(num):
#         prime_factor_list.append(num)
#         prime_factor_power_list.append(1)
#     else:
#         for i in factors:

def prime_factors(num):
    possible_factors = prime_list(num)
    pf_list = []
    power_list = []
    i = 0
    while i < len(possible_factors):
        if not num%possible_factors[i]:
            try:
                list_index = pf_list.index(possible_factors[i])
                power_list[list_index] += 1
            except:
                pf_list.append(possible_factors[i])
                power_list.append(1)
            num = num/possible_factors[i]
        else:
            i += 1
    return pf_list,power_list

def find_all_prime_factors(num, prime_factor_list=[], prime_factor_power_list=[], factor=2):
    """find all the prime factors of a given number, a helper for get_prime_factor_list"""
    while factor!=num:
        if not num%factor:
            location = prime_factor_list.index(factor)
            prime_factor_power_list[location] += 1
            return find_all_prime_factors(num/factor,prime_factor_list, prime_factor_power_list, factor)
        factor+=1

    location = prime_factor_list.index(factor)
    prime_factor_power_list[location] += 1
    return prime_factor_list, prime_factor_power_list

# test area
# print n_factorial_prime_factor_list(8)