class Solution:
    memo = {}
    def superEggDrop(self, m: int, n: int) -> int:
        if m == 1: return n
        if n == 0 or n == 1: return n
        if (m, n) in self.memo:
            return self.memo[(m, n)]
        low, high = 1, n
        while low + 1 < high:
            mid = (low + high) // 2
            t1 = self.superEggDrop(m - 1, mid - 1)
            t2 = self.superEggDrop(m, n - mid)
            if t1 < t2:
                low = mid
            elif t1 > t2:
                high = mid
            else:
                low = high = mid
        ans = 1 + min(max(self.superEggDrop(m - 1, k - 1), self.superEggDrop(m, n - k)) for k in (low, high))
        self.memo[(m, n)] = ans
        return ans
    
    
# My Solution

class Solution:
    memo=[[-1 for i in range(101)] for j in range(10001)]
    def superEggDrop(self, m: int, n: int) -> int:
        if m==1: return n
        if n==0 or n==1: return n
        ans = 10e9
        if self.memo[m][n]!= -1:
            return self.memo[m][n]
        for k in range(1,n):
            temp_ans = 1+max(self.superEggDrop(m,n-k), self.superEggDrop(m-1,k-1))
            if temp_ans<ans: ans=temp_ans
        self.memo[m][n] = ans
        return ans