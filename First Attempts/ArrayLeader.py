'''You are given an array arr of positive integers. Your task is to find all the leaders in the array. 
An element is considered a leader if it is greater than or equal to all elements to its right. 
The rightmost element is always a leader.
'''

'''Input: Array
Check Array[i] against all righthand elements
if >; then leader
else, break and repeat for Array[i+1]
'''

def array_leader(this_list):
    result = []
    pos = 0

    for i in this_list:
        flag = False
        counter = pos
        while (flag == False) & (counter < len(this_list)):
            if (this_list[pos]< this_list[counter]):
                flag = True
            else:
                counter += 1
        if flag == False:
            result.append(i)
        pos += 1
    return result

def array_leader_mod(this_list):
    result = []
    current_leader = -1

    for i in this_list[::-1]:
        if (i >= current_leader):
            current_leader = i
            result.append(i)
    return result[::-1]

test_array1 = [16, 17, 4, 3, 5, 2]
test_array2 = [10, 4, 2, 4, 1]
test_array3 = [5, 10, 20, 40]
test_array4 = [30, 10, 10, 5]
print(f"Array Leaders for Test 1: {array_leader(test_array1)}")
print(f"Array Leaders for Test 2: {array_leader(test_array2)}")
print(f"Array Leaders for Test 3: {array_leader(test_array3)}")
print(f"Array Leaders for Test 4: {array_leader(test_array4)}")
print(f"\nModified Array Leaders for Test 1: {array_leader_mod(test_array1)}")
print(f"Modified Array Leaders for Test 2: {array_leader_mod(test_array2)}")
print(f"Modified Array Leaders for Test 3: {array_leader_mod(test_array3)}")
print(f"Modified Array Leaders for Test 4: {array_leader_mod(test_array4)}")