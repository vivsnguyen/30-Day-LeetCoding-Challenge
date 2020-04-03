"""
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest 
sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer 
approach, which is more subtle.
"""
def max_sub_array(nums):
    overall_max = max(nums)
    current_max = min(nums)

    #if all numbers positive
    if all([True if num > 0 else False for num in nums]):
        return sum(nums)

    #if all numbers negative
    elif all([True if num < 0 else False for num in nums]):
        return overall_max

    for num in nums:
        current_max = max(num, current_max + num)
        overall_max = max(current_max, overall_max)

    return overall_max

def max_sub_array_divide_and_conquer(nums):
    pass
