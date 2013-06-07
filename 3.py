# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factors(num,factor=2):
    while factor!=num:
        if not num%factor:
            return largest_prime_factors(num/factor,factor)
        factor+=1
    return factor

print largest_prime_factors(600851475143)
