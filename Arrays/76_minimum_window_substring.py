'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

def minWindow(s,t):
    if t=="": return ""
    countT,window = {},{}
    for i in t:
        countT[i] = countT.get(i,0) + 1
    res = [-1,-1]
    resLen = float("infinity")
    left = 0
    have, need = 0,len(countT)
    
    for right in range(len(s)):
        c = s[right]
        
        window[c] = window.get(c,0)+1
        
        if c in countT and window[c] == countT[c]:
            have+=1
        
        while have == need:
            if (right-left+1)<resLen:
                res = [left,right]
                resLen = right-left+1
            window[s[left]]-=1
            
            if s[left] in countT and window[s[left]] <countT[s[left]]:
                have-=1
            left+=1
    left,right = res
    return s[left:right+1] if resLen != float("infinity") else ""


s= "ADOBECODEBANC"
t = "ABC"
result  = minWindow(s,t)
print("result: ",result)