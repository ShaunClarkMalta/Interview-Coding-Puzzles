'''You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). 
This array represents a permutation of the integers from 1 to n with one element missing. 
Your task is to identify and return the missing element.'''

'''Sum of n consecutive integers = (n*(n+1)/2)
Take length of array, and add 1 (Missing element)
Calculate Expected Sum
Calculate Actual Sum
Difference is Missing Integer'''

def missing_integer(this_list):
    n = len(this_list)+1
    expected_sum = (n*(n+1))/2
    actual_sum = 0

    for i in this_list:
        actual_sum = actual_sum + i

    result = expected_sum - actual_sum
    return result

example_list = [1,2,3,5,6,7,8,9]
result = missing_integer(example_list)
print(f"The Missing Integer is: {result}.")

test1 = [1,2,3,5]
test2 = [8, 2, 4, 5, 3, 7, 1]
test3 = [1]
print(f"Test 1 - Missing Integer: {missing_integer(test1)}")
print(f"Test 2 - Missing Integer: {missing_integer(test2)}")
print(f"Test 3 - Missing Integer: {missing_integer(test3)}")