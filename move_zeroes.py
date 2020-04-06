"""
Given an array nums, write a function to move all 0's 
to the end of it while maintaining the relative order 
of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Hint #1: In-place means we should not be allocating any space 
for extra array. But we are allowed to modify the existing array. 
However, as a first step, try coming up with a solution that makes 
use of additional space. For this problem as well, first apply 
the idea discussed using an additional array and the in-place 
solution will pop up eventually.

Hint #2: A two-pointer approach could be helpful here. 
The idea would be to have one pointer for iterating the array 
and another pointer that just works on the non-zero elements 
of the array.
"""

def move_zeroes_not_in_place(nums):
    new_nums = []
    zeroes_count = 0
    
    for num in nums:
        if num != 0:
            new_nums.append(num)

        else:
            zeroes_count += 1
    
    new_nums.extend([0]*zeroes_count)

    return new_nums


def move_zeroes(nums):

    index = 0
    num_zeroes = 0

    while index < len(nums):
        if nums[index] == 0:
            nums.pop(index)
            num_zeroes += 1
            continue

        index += 1

    nums.extend([0]*num_zeroes)

    return nums