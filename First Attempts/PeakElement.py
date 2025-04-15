'''Given an array arr[] where no two adjacent elements are same, find the index of a peak element. 
An element is considered to be a peak if it is greater than its adjacent elements (if they exist). If there are multiple peak elements, return index of any one of them. 
The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".'''

'''Using Binary Search
- Check 1st Element
- Check Last Element
- Check Middle Element
- If array[mid] > array [mid-1]; Go right
- Else if array [mid] < array [mid-1]; Go left'''

def peak_element(this_list):
    if (len(this_list) == 1):             #Case if only 1 element in list
        return 0
    elif (this_list[0] > this_list[1]):       #If the first position is greater than the second, then it is a peak
        return 0
    elif (this_list[-1]) > this_list[-2]:   #If the last position is greater than the penultimate, then it is a peak
        return (len(this_list)-1)
    else:
        left = 1                            #Can already exclude pos 0 from search
        right = (len(this_list)-2)          #Can already exclude pos[-1] from search
        
        while left <= right:
            mid = left + (right-left)//2
            if (this_list[mid] > this_list[mid-1]) & (this_list[mid] > this_list[mid+1]):   #If Midpoint is greater than its left (mid-1) and right (mid+1) components, return it as the peak
                return mid
            elif (this_list[mid] > this_list[mid-1]):       #If greater than left-side, then must go right. Can already exclude mid as an option
                left = mid+1
            else:
                right = mid-1

test_array1 = [1, 2, 4, 5, 7, 8, 3]
test_array2 = [10, 20, 15, 2, 23, 90, 80]
test_array3 = [1, 2, 3]
test_array4 = [10, 2, 3]
test_array5 = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
print(f"Test Array 1 has a peak at: {peak_element(test_array1)}")
print(f"Test Array 2 has a peak at: {peak_element(test_array2)}")
print(f"Test Array 3 has a peak at: {peak_element(test_array3)}")
print(f"Test Array 4 has a peak at: {peak_element(test_array4)}")
print(f"Test Array 5 has a peak at: {peak_element(test_array5)}")