'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        max_len = 0
        seen = []
        while j < len(s):
            if s[j] not in seen:
                seen.append(s[j])
                j += 1
                max_len = max(max_len, j - i)
            else:
                seen.remove(s[i])
                i += 1
        return max_len
    
# Solution 2 ( Most optimised version )

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alphabet = {}
        ans = 0
        n = len(s)
        start = 0
        
        for index, letter in enumerate(s):
            if letter in alphabet:
                sums = alphabet[letter] + 1
                if sums > start:
                    start = sums
            
            num = index - start + 1
            if num > ans:
                ans = num
            
            alphabet[letter] = index
        
        return ans



