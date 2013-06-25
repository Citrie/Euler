# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import math

def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if not num%i: return False
    return True

n, count = 2, 0
while count<10001:
    if is_prime(n):
        count+=1
    n+=1

print n-1
