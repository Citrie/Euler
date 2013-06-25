# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import math

def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if not num%i: return False
    return True


n, i = 0, 2
twomillion = 2000000

while i < twomillion:
    if is_prime(i): 
        n+=i
    i+=1

print n

