'''
Create an algorithm to find a substring with the maximum length that contains precisely K distinct characters within a given string. 
If multiple substrings have the same maximum length, you can output any one of them.

Your Task: You don't need to read input or print anything. 
Your task is to complete the function longestKSubstr() 
which takes the string S and an integer K as input and returns the length of the longest substring with exactly K distinct characters.
If there is no substring with exactly K distinct characters then return -1.

Sample Input
S = "aabacbebebe", K = 3
Sample Output
7
Explanation
"cbebebe" is the longest substring with 3 distinct characters.
Constraints:
1 <= s.length <= 1e^6
'-a' <= s[i] <= 'z'
K <= 26
'''

# My solution @BruteForce O(n^2).
class Solution:
  def longestKSubstr(self, s, k):
    i,j = 0,0
    max_len = -1
    while j<len(s):
      set_len = len(set(s[i:j+1]))
      if set_len == k:
        max_len = max(max_len,j-i+1)
        j+=1
      elif set_len > k:
        i+=1
      else:
        j+=1
    return max_len


# More optimized solution. Time complexity is O(n) @SlidingWindow
class Solution2:
    def longestKSubstr(self, s, k):
        if k > len(set(s)):
            return 0

        char_freq = {}
        max_len = 0
        unique_chars = 0
        left = 0

        for right in range(len(s)):
            char_freq[s[right]] = char_freq.get(s[right], 0) + 1

            if char_freq[s[right]] == 1:
                unique_chars += 1

            while unique_chars > k:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    unique_chars -= 1
                left += 1

            if unique_chars == k:
                max_len = max(max_len, right - left + 1)

        return max_len