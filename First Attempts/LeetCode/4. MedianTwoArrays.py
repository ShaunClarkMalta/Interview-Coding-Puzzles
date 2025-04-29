'''Median of Two Sorted Arrays
Hard
Topics
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.'''

'''First thoughts; To merge the two and sort; I realise that this is not the most optimal for longer arrays
Having done research, need to use a Binary Search Tree.

length = len(n) + len(m)
- Take length/2 left-hand elements from list 1,, Same from list 2 (If odd number, take from list 1)
- Check that max in both lists < min of leftover elements
- Adjust pointers accordingly and repeat'''
