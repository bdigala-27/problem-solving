def pp(s,i,j):
    if i>=j:
        return 0
    if is_palindrome(s,i,j):
        return 0
    ans = 10e9
    for k in range(i,j):
        temp_ans = 1+pp(s,i,k)+pp(s,k+1,j)
    if temp_ans<ans:
        ans = temp_ans
    return ans
def is_palindrome(s,i,j):
    return s[i:j] == s[i:j:-1]

s="sagar"
i = 0
j = len(s)-1
print(pp(s,i,j))