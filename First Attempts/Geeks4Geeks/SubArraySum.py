'''
Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) 
whose sum equals a specified value target. 
You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. 
You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].'''

'''Input: Array, Target
Pos[0] < Target? 0 + 1,, repeat 
Pos[0] > Target? counter +1

End = -1 if none,, [Start(+1), End(+1)]'''

def subarray_sum(this_list, target):
    result = [-1]
    pos = 0

    for i in this_list:
        total = i
        counter = 0
        pos +=1
    
        while (total <= target):
            if (total == target):
                result = [pos, pos+counter]
                return result
            total = total + this_list[pos+counter]
            counter = counter + 1
        if pos == (len(this_list)):
            return result

first_array = [1, 2, 3, 7, 5] 
target1 = 12
second_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target2 = 15
third_array = [5, 3, 4]
target3 = 2
print(f"First Test: {subarray_sum(first_array, target1)}")
print(f"Second Test: {subarray_sum(second_array, target2)}")
print(f"Third Test: {subarray_sum(third_array, target3)}")