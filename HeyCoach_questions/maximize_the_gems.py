'''
You're an adventurous spelunker exploring a treasure-filled cavern. Each chamber holds a precious gem marked with an integer value. 
Your goal? Maximize your haul by strategically collecting these gems!

Explore the cave, represented by an integer array nums. Each element nums[i] represents the value of a gem in the chamber i. 
You can claim a gem (delete nums[i]) and earn points equal to its value. But there's a catch! When you claim a gem: 
All gems in other chambers with values one less than your chosen gem (i.e., nums[j] = nums[i] - 1) crumble instantly and disappear. 
All gems in other chambers with values one more than your chosen gem (i.e., nums[j] = nums[i] + 1) also crumble and vanish. 
Your mission is to maximize the total points you earn by strategically claiming gems. You can claim any gem any number of times (until it's gone!).

Input/Output Format Examples:
Input:
[3, 4, 2] (Cave chambers with gem values)

Output:
6 (Maximum points earned by strategically claiming gems)

Explanation:
You can claim:

Gem 4 from chamber 1, earning 4 points and causing chambers 2 and 3 (containing gems 3 and 5) to crumble.
Gem 2 from the remaining chamber, earning 2 points.

Input:1
A single line containing an integer array nums separated by spaces or commas. Each element in nums is an integer between 1 and 10^4 (inclusive). 
The length of nums (n) must be between 1 and 2 * 10^4 (inclusive).

Output:
return a single integer representing the maximum number of points you can earn by claiming gems in the cave according to the described rules.

Constraints:
1 <= n <= 2 * 10^4

1 <= nums[i] <= 10^4 for all i in [0, n-1]
'''

class Solution:
    def deletePoints(self, nums):
        # Initialize a dictionary to store the total points for each gem value
        points = {}
        for num in nums:
            # For each gem, add its value to the corresponding entry in the dictionary
            points[num] = points.get(num, 0) + num

        # Initialize variables for the previous two gem values and their maximum points
        prev1, prev2 = 0, 0
        for num in sorted(points):
            # If the current gem value is not consecutive with the previous gem value
            if num - 1 != prev1:
                # The maximum points for the current gem value is its points plus the maximum points for the previous gem value
                points[num] += points.get(prev1, 0)
            else:
                # If the current gem value is consecutive with the previous gem value
                # The maximum points for the current gem value is its points plus the maximum points for the gem value before the previous gem value
                points[num] += points.get(prev2, 0)

            # Update the previous two gem values
            prev2, prev1 = prev1, num

        # Return the maximum points for the last gem value
        return max(points.get(prev1, 0), points.get(prev2, 0))

s=Solution()
nums=[3,4,2]
ans = s.deletePoints(nums)
print(ans)