"""
Suppose an array sorted in ascending order is rotated 
at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in 
the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the 
order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

def search(nums, target):
    if not nums:
            return -1
        
    min_index = 0
    max_index = len(nums) - 1
    
    while min_index <= max_index:
        mid_index = max_index + min_index // 2

        if nums[mid_index] == target:
            return mid_index

         if mid_index > target:
            # Target is to the left, so move ceiling to the left
            max_index = guess_index
        else:
            # Target is to the right, so move floor to the right
            min_index = guess_index

    return -1