import math

list=range(10)
final_num = []

million = 999999
for i in range(10): # record the digits, first calculate the first one
    digit = 10 - i
    index = int(million/math.factorial(digit-1))
    print index
    num = list[index]
    final_num.append(num)
    list.remove(num)
    million -= index * int(math.factorial(digit-1))

print final_num
