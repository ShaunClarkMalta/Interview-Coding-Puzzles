'''You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

For example:

If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
If arr[i] = 0, you cannot jump forward from that position.
Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

Note:  Return -1 if you can't reach the end of the array.'''

'''Input Array
x = array[i]
if x = 0; result = -1
largest [i+1, ... i+x]
jumps += 1'''

'''def min_jumps(this_list):
    result = 0
    pos = 0
    end_flag = len(this_list)-1

    if this_list[0] == 0:
        result = -1
        return result
    while (pos < end_flag):
        jumps = this_list[pos]
        subset_list = this_list[(pos+jumps):pos:-1]
        maximum = max(subset_list)
        pos = pos + (len(subset_list)-subset_list.index(maximum))
        result +=1
    return result'''

def min_jumps(this_list):
    jumps = 1
    max_reach = 0
    current_reach = 0
    pos = 0
    result = -1
    end_list = (len(this_list) -1)
    
    if (this_list[0] == 0):
        return result
    
    while (max_reach < end_list):
        max_reach = pos + this_list[pos]
        counter = 1
        jumps += 1
        subset_list = this_list[pos+1:(max_reach+1):]
        for i in subset_list:
            current_reach = i + (pos + counter)
            if current_reach > max_reach:
                max_reach = current_reach
                step = pos + counter
            counter += 1
        pos = step
    result = jumps
    return result

test1 = [1,3,8,5,8,9,2,6,7,6,8,9,5,7,6,5,1,5,4,2,3,1]
test2 = [1, 4, 3, 2, 6, 7]
test3 = [0, 10, 20]
print(f"Result for Test 1: {min_jumps(test1)}")
print(f"Result for Test 2: {min_jumps(test2)}")
print(f"Result for Test 3: {min_jumps(test3)}")

test_array1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
test_array2 = [1, 4, 3, 2, 6, 7]
test_array3 = [0, 10, 20]
print(f"Array 1: Minimum Jumps - {min_jumps(test_array1)}")
print(f"Array 2: Minimum Jumps - {min_jumps(test_array2)}")
print(f"Array 3: Minimum Jumps - {min_jumps(test_array3)}")

#I believe that this is wrong and I need to look into a better solution - Have a better solution on paper, and need to implement it
