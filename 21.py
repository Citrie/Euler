from lib import find_all_factors

list = [0] * 10000

# initialize list
for i in range(10000):
    list[i] = sum(find_all_factors(i+1))-i-1
print list[219], list[283]

# check amicable numbers
sumup = 0
for i in range(10000): # the actual number is i+1
    j = list[i]
    if j-1 in range(10000) and list[j-1] == i+1 and i+1!=j:
        sumup +=i+1
        print i,j
print sumup