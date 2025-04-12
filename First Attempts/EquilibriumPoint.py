'''Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. 

Return -1 if no such point exists. '''

'''
Input: Array
Right-Hand = Sum(array)
Left-Hand = 0
at array[i]:
Right-hand = Sum - array[i]
Left-hand += array[i-1]
if Left == Right:
    return counter
else:
    -1'''

def equilibrium_point(this_list):
    left_count = 0
    right_count = sum(this_list)
    counter = 0

    for i in this_list:
        if counter == 0:
            left_count = 0
        else:
            left_count += this_list[counter-1]
        right_count -= i
        if (left_count == right_count):
            return counter
        else:
            counter += 1
    return -1 #There is no equilibrium point

test_array1 = [1, 2, 0, 3]
test_array2 = [1, 1, 1, 1]
test_array3 = [-7, 1, 5, 2, -4, 3, 0]
test_array4 = [1, 2, 0, 3, 0]
test_array5 = [3, 6, 9, 12, 8, 4, 2, 8, 16]
print(f"The Equilibrium Point for Array 1 is: {equilibrium_point(test_array1)}")
print(f"The Equilibrium Point for Array 2 is: {equilibrium_point(test_array2)}")
print(f"The Equilibrium Point for Array 3 is: {equilibrium_point(test_array3)}")
print(f"The Equilibrium Point for Array 4 is: {equilibrium_point(test_array4)}")
print(f"The Equilibrium Point for Array 5 is: {equilibrium_point(test_array5)}")