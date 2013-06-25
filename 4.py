# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_divisible_by_3_digit(num):
    for i in range(100,1000):
        if not num%i and num/i in range(100,1000): 
            return True
    return False

def is_palindrome(str):
    for i in range(len(str)):
        if str[i]!=str[-(i+1)]: return False
    return True

for n in range(999*999,100*100,-1):
    if is_divisible_by_3_digit(n) and is_palindrome(str(n)): 
        print n
        break
