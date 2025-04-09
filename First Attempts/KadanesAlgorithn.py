'''Given an integer array arr[]. You need to find the maximum sum of a subarray.'''

'''Maximum of array = Sum
Check pos [i]  > max?
pos [i] + ... >max?'''

def max_subarray(this_list):
    max_sum = sum(this_list)
    pos = 0
    for i in this_list:
        counter = 0
        total = 0
        while ((pos+counter) < len(this_list)):
            total = total + this_list[pos+counter]
            if (total > max_sum):
                max_sum = total
            counter +=1
        pos += 1
    return max_sum

test_array1 = [2, 3, -8, 7, -1, 2, 3]
test_array2 = [-2, -4]
test_array3 = [5, 4, 1, 7, 8]
print(f"Maximum in Array 1 of Sub-Array is {max_subarray(test_array1)}")
print(f"Maximum in Array 2 of Sub-Array is {max_subarray(test_array2)}")
print(f"Maximum in Array 3 of Sub-Array is {max_subarray(test_array3)}")