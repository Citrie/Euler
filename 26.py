def smallest_9(num,start=9):
    if not start%num:
        return start
    else:
        start=10*start+9
        return smallest_9(num,start)

recurring_list = [0] * 1000

for i in range(1000):
    actual_i = i + 1
    if actual_i%5 and actual_i%2:
        recurring_list[i] = smallest_9(actual_i)

print max(recurring_list)
print recurring_list.index(max(recurring_list))+1



# print smallest_9(7)