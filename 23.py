#28123
from lib import find_all_factors
abundant_list = []
for i in range(28124):
    if sum(find_all_factors(i+1))-i-1>i+1:
        abundant_list.append(i+1)


list_len = len(abundant_list)
print list_len

list_two_abundant_sum_list = []
for i in range(list_len):
    for j in range(i,list_len):
        abundant_sum = abundant_list[i]+abundant_list[j]
        if abundant_sum < 28124: list_two_abundant_sum_list.append(abundant_sum)

print 28123*(1+28123)/2 - sum(list(set(list_two_abundant_sum_list)))