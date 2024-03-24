'''
In the bustling city of Bangalore, there exists a prestigious coding academy named HeyCoach. This academy is renowned for nurturing brilliant young minds and turning them into skilled programmers and problem solvers. Among the students is Varshil, a diligent and passionate learner who is always eager to explore new challenges.

One day, as Varshil is working on an advanced algorithms assignment, their mentor, Professor Prateek, notices their enthusiasm and decides to present them with a perplexing puzzle. Professor Prateek hands Varshil a piece of paper with a jumble of lowercase alphabetical characters, both a pattern and a text.

"Varshil," Professor Prateek says with a smile, "I have a challenge for you. I want you to find all the indices where this pattern appears within the text."

Help Varshil solve this problem.

Input:

- A string text (1 <= |text| <= 10^5): A jumble of lowercase alphabetical characters.
- A string pattern (1 <= |pattern| <= 10^5): The pattern to search within the text.
Output:

A list of integers representing the indices where the pattern appears within the text. If 
Example 1:

Input:

- text = "ababcabab"
- pattern = "ab"
Output:

[0, 2, 5, 7]
Explanation:

The pattern "ab" appears at indices 0, 2, 4, and 7 within the text.
Constraints:

- 1 <= |text| <= 10^5

- 1 <= |pattern| <= 10^5

1 <= |text| <= 10^5

1 <= |pattern| <= 10^5

The input consists of lowercase alphabetical characters.
'''


# My solution BruteForce
class Solution:
  def findPatternIndices(self, text, pattern):
    n = len(pattern)
    res=[]
    for i in range(len(text)):
      if text[i:n+i] == pattern:
        res.append(i)
    return res



#Optimized solution using KMP alogorithm to find pattern in text

class Solution2:
    def computeLPSArray(self, pattern, M, lps):
        length = 0
        lps[0] = 0
        i = 1
        while i < M:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1

    def findPatternIndices(self, text, pattern):
        N = len(text)
        M = len(pattern)
        lps = [0]*M
        j = 0
        self.computeLPSArray(pattern, M, lps)
        i = 0
        res = []
        while i < N:
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == M:
                res.append(i-j)
                j = lps[j-1]
            elif i < N and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return res
