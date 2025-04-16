'''Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

You need to solve this problem without utilizing the built-in sort function.'''

'''Input array
Create result empty
for i in array;
if 0, then insert at front
if 2, then insert at end
if 1, insert middle - 1 marker
output result'''

def sort012(this_list):
    result = []
    one_marker = 0

    for i in this_list:
        if (i == 2):
            result.append(i)
        elif (i == 0):
            result.insert(0, i)
            one_marker += 1
        elif (i == 1):
            result.insert(one_marker, i)
        else:
            print("Invalid Number")
    return result

test_list1 = [0, 1, 2, 0, 1, 2]
test_list2 = [0, 1, 1, 0, 1, 2, 1, 2, 3, 0, 0, 0, 1]
print(f"Test List 1 sorted is: {sort012(test_list1)}")
print(f"Test List 2 sorted is: {sort012(test_list2)}")