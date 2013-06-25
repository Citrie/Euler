import math

sumup = 0
for i in range(2,1000000):
    str_i = str(i)
    calculate = 0
    for j in str_i:
        calculate += int(math.pow(int(j),5))
    if i == calculate:
        print i
        sumup += i

print sumup

# 4150
# 4151
# 54748
# 92727
# 93084
# 194979
# 443839
# [Finished in 7.9s]

