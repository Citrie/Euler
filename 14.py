# The following iterative sequence is defined for the set of positive integers:

# n  n/2 (n is even)
# n  3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

def mark_chain_length(list, len_list, index):
    rest_length = len_list[index]
    current_chain_length = len(list)
    for elem in list:
        len_list[elem-1] = current_chain_length + rest_length
        current_chain_length -= 1
    return len_list


onemillion = 1000000
# mark_list = [1] * onemillion # 1 means number that never been calculated before, 0 means pass
len_list = [0] * onemillion * 10000
overflow_index_list = []
overflow_len_list = []
len_list[0] = 1
for i in range(onemillion): # i is the index, the actual number is i+1
    if not i%10: print "processing", i
    if len_list[i] != 0: # already been calculated
        # print "skipping", i+1
        i += 1 # check next number
    else: # calculate the length
        actual_i = i+1
        temp_chain = []
        # print i, actual_i, temp_chain
        while actual_i!= 1:
            if actual_i%2: # i is odd
                temp_chain.append(actual_i)
                # print 'now at', i+1, actual_i, temp_chain
                actual_i = actual_i*3+1
            else: # i is even
                temp_chain.append(actual_i)
                # print 'now at', i+1, actual_i, temp_chain
                actual_i /= 2

            if (actual_i-1) < onemillion*100 and len_list[actual_i-1]!=0: # new actual_i has been calculated
                rest_length = len_list[actual_i-1]
            # else if actual_i - 1 >= onemillion*10 and actual_i - 1 in overflow_index_list:
                # rest_length = overflow_len_list[overflow_index_list.index(actual_i - 1)]
                current_chain_length = len(temp_chain)
                for elem in temp_chain:
                    if len_list[elem-1]!=0: len_list[elem-1] = current_chain_length + rest_length
                    current_chain_length -= 1

        # when everything is new and its looping to the ebd
        current_chain_length = len(temp_chain)
        rest_length = len_list[actual_i-1]
        # print 'actual_i', actual_i, 'current_chain_length', current_chain_length, 'rest_length', rest_length
        for elem in temp_chain:
            len_list[elem-1] = current_chain_length + rest_length 
            # print 'put # ', elem, 'to', len_list[elem-1]
            current_chain_length -= 1
        actual_i = 1

onemillion_list = len_list[:onemillion]
longest_chain = max(onemillion_list)
print longest_chain
print onemillion_list.index(longest_chain)