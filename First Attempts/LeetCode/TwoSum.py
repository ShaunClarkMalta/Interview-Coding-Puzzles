'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

'''Create a hash table/ dictionary - {number: index}
x = target - y
Check if x is in dictionary;
else: add and next integer'''

def two_sum(number_array, target):
    seen = {}                   
    result = -1            #Creates Table
    for i in range(len(number_array)):      #Traverses array
        diff = target - i                   #What we are looking for
        if diff in seen:                    #If diff exists in seen, it means we have already found it
            result = seen[diff], i          #If so, then return first_index, current_index
            return result
        else:
            seen[number_array[i]] = diff        #Sets Seen Dictionary [i] and its value
    return result


test_array1 = [2,4,9,6,5]
target1 = 10
print(f"Target {target1} in Test Array 1: {two_sum(test_array1,target1)}")
test_array2 = [1,2,5,8,3]
target2 =13
print(f"Target {target2} in Test Array 2: {two_sum(test_array2,target2)}")
test_array3 = [4,3,6,8,7,9]
target3 = 13
print(f"Target {target3} in Test Array 3: {two_sum(test_array3,target3)}")