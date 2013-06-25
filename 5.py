# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def greatest_common_factor(a,b):
    i = min(a,b)
    while i:
        if not a%i and not b%i: return i
        i-=1

n = 1
for i in range(1,21):
    n *= i/greatest_common_factor(i,n)

print n