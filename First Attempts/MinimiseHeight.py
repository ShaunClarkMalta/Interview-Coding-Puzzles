'''Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.'''

'''Input: Array,, Integer K
Find: Mean of Array (sum/len)
for i in array: if i < mean: add k, else, subtract
Take max and min; subtract

def minimise_heights(this_list, k):
    modified_list = []
    max_value = -999
    min_value = 999

    mean_array = sum(this_list)/len(this_list)

    for i in this_list:
        if i <= mean_array:
            new_value = i+k
        else:
            new_value = i - k
        modified_list.append(new_value)
        if (new_value > max_value):
            max_value = new_value
        if (new_value < min_value):
            min_value = new_value

    return (max_value - min_value)
    
    #Having done research, I see that this is not always the best approach'''

'''Find MAX and MIN values of array. 
Big = MAX - k,, Small = MIN + k
for i in array:
    if i-k OR i+k in range (big, small); Continue
    else: set big/small to newest value'''

def minimise_heights_mod(this_list, k):
    ceiling_value = max(this_list) - k
    floor_value = min(this_list) + k

    for i in this_list:
        addition = i + k
        subtraction = i - k

        if (addition in range(floor_value, ceiling_value+1)) | (subtraction in range(floor_value, ceiling_value+1)):
            continue
        else:
            if (addition - ceiling_value) > (floor_value - subtraction):
                floor_value = subtraction
            elif (floor_value - subtraction) > (addition - ceiling_value):
                ceiling_value = addition
    return (ceiling_value - floor_value)

k = 2
test_array1 = [1, 5, 8, 10]
print(f"Result for Test Array 1: {minimise_heights_mod(test_array1, k)}")
k = 3
test_array2 = [3, 9, 12, 16, 20]
print(f"Result for Test Array 2: {minimise_heights_mod(test_array2, k)}")
k = 6
test_array3 = [1, 15, 10]
print(f"Result for Test Array 3: {minimise_heights_mod(test_array3, k)}")
k = 3
test_array4 = [1, 5, 10, 8]
print(f"Result for Test Array 4: {minimise_heights_mod(test_array4, k)}")