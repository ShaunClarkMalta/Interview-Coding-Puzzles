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

def min_jumps(this_list):
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
    return result

test_array1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
test_array2 = [1, 4, 3, 2, 6, 7]
test_array3 = [0, 10, 20]
print(f"Array 1: Minimum Jumps - {min_jumps(test_array1)}")
print(f"Array 2: Minimum Jumps - {min_jumps(test_array2)}")
print(f"Array 3: Minimum Jumps - {min_jumps(test_array3)}")