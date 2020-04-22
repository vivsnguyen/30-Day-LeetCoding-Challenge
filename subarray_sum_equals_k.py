"""
Given an array of integers and an integer k, you need 
to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] 
and the range of the integer k is [-1e7, 1e7].

   Hide Hint #1  
Will Brute force work here? Try to optimize it.

   Hide Hint #2  
Can we optimize it by using some extra space?

   Hide Hint #3  
What about storing sum frequencies in a hash table? Will it be useful?
   
   Hide Hint #4  
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.
"""

#dictionary
def subarray_sum(nums, k):
        count = 0
        current_sum = 0
        sums_dict = {}
        
        sums_dict[0] = 1 #?
        
        for i in range(len(nums)):
            current_sum += nums[i]
            count += sums_dict.get(current_sum-k,0)
            sums_dict[current_sum] = sums_dict.get(current_sum,0) + 1
            
        return count

