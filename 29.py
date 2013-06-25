# b = b1*b2*b3
# a^b = (a^b1)^b2^b3

# log 2
# 2 (2 -> 100)
# ,4 2*(2 -> 100)
# ,8 3*(2 -> 100)
# ,16
# ,32,
# 64 6*(2 -> 100)

# 3,9,27,81
# 4,16,64
# 5,25
# 6,36
# 7,49
# 8,64
# 9,81
# 10,100

import math
sumup = 0
count = 0
for i in (2,3,5,6,7,10): # 2 -> 10 calculate differently
    current = i
    count_list = []
    while current<=100:
        step = int(math.log(current,i))
        count_list += range(2*step,100*step+1,step)
        current *= i
        count += 1
    count_list = list(set(count_list))
    sumup += len(count_list)

print sumup,count
sumup += (99-count)*99
print sumup

# 1164 18
# 9183
# [Finished in 0.1s]