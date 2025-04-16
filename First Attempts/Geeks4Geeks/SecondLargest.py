'''Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.'''

'''find max(array)
second = 0
if i > second && != max; second = i'''

def second_largest(this_list):
    result = -1
    max_number = max(this_list)
    for i in this_list:
        if (i > result) & (i != max_number):
            result = i
    return result

test_array1 = [12, 35, 1, 10, 34, 1]
test_array2 = [10, 5, 10]
test_array3 = [10, 10, 10]
print(f"The 2nd largest number in Array 1 is: {second_largest(test_array1)}")
print(f"The 2nd largest number in Array 2 is: {second_largest(test_array2)}")
print(f"The 2nd largest number in Array 3 is: {second_largest(test_array3)}")