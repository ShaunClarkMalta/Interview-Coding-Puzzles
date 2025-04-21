'''Given three sorted arrays in non-decreasing order, print all common elements in non-decreasing order across these arrays. 
If there are no such elements return an empty array. In this case, the output will be -1.

Note: can you handle the duplicates without using any additional Data Structure?'''

'''Input: Three sorted arrays
Create 3 pointers for the arrays
if array1[p1] == array2[p2] == array3[p3]:
    add to results list
else:
    array1[p1] < array2[p2]?:
        p1 +1 
    array2[p2] < array3[p3]?:
        p2 +1
    else:
        p3 +1'''

def common_num(this_list1, this_list2, this_list3):
    #Create a pointer for each list, and a final list storing the result
    pointer1 = 0
    pointer2 = 0
    pointer3 = 0
    results = []

    #Loop checking the lists 1 by 1 to see if the numbers are the same
    while ((pointer1 < len(this_list1)) and (pointer2 < len(this_list2)) and (pointer3 < len(this_list3))):
        #If all three are pointing at the same number, then you can add to the results and incrememnt all pointers by 1 to look at the next element
        if this_list1[pointer1] == this_list2[pointer2] == this_list3[pointer3]:
            results.append(this_list1[pointer1])
            pointer1 += 1
            pointer2 +=1
            pointer3 +=1
        #How to proceed if numbers are not the same
        else:
            #If pointer1 is still in range of the list, and has the lowest value
            if (this_list1[pointer1] < this_list2[pointer2]):
                pointer1 += 1
            elif (this_list2[pointer2] < this_list3[pointer3]):
                pointer2 += 1
            else:
                pointer3 += 1

    #At end, either return result = -1, or result list
    if len(results) == 0:
        return -1
    else:
        return results
    
array1 = [1, 5, 10, 20, 30]
array2 = [5, 13, 15, 20]
array3 = [6, 20]
print(f"The results are: {common_num(array1, array2, array3)}")

array1 = [2, 5, 10, 30]
array2 = [5, 13, 19]
array3 = [5, 20, 34]
print(f"The results are: {common_num(array1, array2, array3)}")

array1 = [1,3,4,5]
array2 = [3,5,7,9]
array3 = [3,6]
print(f"The results are: {common_num(array1, array2, array3)}")