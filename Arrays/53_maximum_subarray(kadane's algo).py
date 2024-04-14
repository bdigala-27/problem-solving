'''
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''


# The below approach is the Kadane's algorithm

class Solution:
    def max_sub_array(self,nums):
        n = len(nums)
        max_sum = float('-inf')
        curr_sum = 0
        
        for i in range(n):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
    
    def max_sub_array2(self, nums):
        max_sum = curr_sum = nums[0]
        
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
    
s= Solution()

nums = [5,4,-1,7,8]

ans = s.max_sub_array(nums)

print(ans)