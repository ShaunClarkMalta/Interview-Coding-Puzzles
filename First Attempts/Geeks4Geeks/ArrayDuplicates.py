'''Given an array arr of integers, find all the elements that occur more than once in the array. If no element repeats, return an empty array.'''

'''Input original array
Create empty set,, create list duplicates
for i in original:
    if i in set; append to list_duplicates'''

def array_duplicates(this_list):
    #result = [] #if you want all duplicates in a list
    result = set() #If you just want a list with all repeated values
    set_values = set()
    for i in this_list:
        if i in set_values:
            result.add(i)
        else:
            set_values.add(i)
    return list(result)

test_list1 = [2, 3, 1, 2, 3]
test_list2 = [0, 3, 1, 2]
test_list3 = [2, 4, 6, 7 , 8, 9, 2, 4, 6, 7, 4, 5]
print(f"Test List 1 - {array_duplicates(test_list1)}")
print(f"Test List 2 - {array_duplicates(test_list2)}")
print(f"Test List 3 - {array_duplicates(test_list3)}")