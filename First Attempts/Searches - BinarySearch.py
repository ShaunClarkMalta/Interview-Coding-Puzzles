'''Binary Search - Extremely Efficient
Must have an ordered list (Either Ascending or Descending)
Compares the search to the Middle value, then recalculates'''

def binary_search(target, this_list):
    left = 0
    right = len(this_list) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left)//2 #Calculate mid point
        if this_list[mid] == target:
            result = mid
            right = mid - 1
        
        elif mid > target:  #Then must be to the left array
            right = mid - 1

        elif mid < target: #Must be in the right array
            left = mid + 1

    return result #If target not found

k = 4
test_array1 = [1, 2, 3, 4, 5]
print(f"Value {k} in Test Array 1 is at index: {binary_search(k, test_array1)}")
k = 445
test_array2 = [11, 22, 33, 44, 55]
print(f"Value {k} in Test Array 2 is at index: {binary_search(k, test_array2)}")
k = 1
test_array3 = [1, 1, 1, 1, 2]
print(f"Value {k} in Test Array 3 is at index: {binary_search(k, test_array3)}")