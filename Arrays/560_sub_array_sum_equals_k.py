class Solution:
    def subarraySum(self, nums, k):
        hash = {0:1}
        i,sum,res = 0, 0 ,0
        for i in nums:
            sum+=i
            if sum-k in hash:
                res+=hash[sum-k]
            hash[sum] = hash.get(sum,0)+1
        return res
# more efficient solution

class Solution2:
    def subarraySum(self, nums, k):
        hash = {0:1}
        sum,res =  0 ,0
        for i in nums:
            sum+=i
            diff = sum-k
            res += hash.get(diff,0) #it will add the diff if it is there in the hash or else it will add 0.
            hash[sum] = 1+hash.get(sum,0)
        return res
    
    
nums = [1,2,3]
k = 3
s = Solution()
ans = s.subarraySum(nums,k)
print(ans)
        