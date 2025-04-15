'''You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.'''


def subset_sum(array_numbers, target_sum):
    num_count = len(array_numbers)
    
    dp = [[False] * (target_sum + 1) for _ in range(num_count + 1)]     #Creates a DynamicProgramming table of target+1*num+1 cells, all FALSE
    for i in range(num_count+1):
        dp[i][0] = True                                                 #Sets all 0 column to True, as it is always valid
    for item_index in range(1, num_count+1):
        current_number = array_numbers[item_index-1]                    #Loops through all numbers (except 0). Sets current number to the value at the index(minus 1) in the array
        for current_sum in range(1, target_sum+1):
            exclude = dp[item_index - 1][current_sum]                   #If it could already be True, then it is ignored
            include = False
            if current_number <= current_sum:                           #If the Current Number is less than the current sum, then it can be included as True
                include = dp[item_index - 1][current_sum - current_number]
            dp[item_index][current_sum] = include or exclude            #If either Include or Exclude are True, then it is included in the table
    for row in dp:
        print(['T' if cell else 'F' for cell in row])
    return dp[num_count][target_sum]

array1 = [4,2,5]
target = 11
print(f"Test Array 1: {subset_sum(array1, target)}")