from collections import deque
def next_greater_element_to_right(arr,n):
    res=[]
    stack = deque()
    
    for i in range(n-1,-1,-1):
        if len(stack)==0:
            res.append(-1)
        elif (len(stack)>0 and stack[-1]>arr[i]):
            res.append(stack[-1])
        elif (len(stack)>0 and stack[-1]<=arr[i]):
            while (stack and stack[-1]<=arr[i]):
                stack.pop()
            if (len(stack)==0):
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(arr[i])
    return res[::-1]

#More optimized solution.
def next_greater_element_to_right2(arr, n):
    res = [-1] * n
    stack = deque()

    for i in range(n-1, -1, -1):
        while stack and arr[i] >= stack[-1]:
            stack.pop()

        if stack:
            res[i] = stack[-1]

        stack.append(arr[i])

    return res


arr = [1,3,0,0,1,2,4,9,7]
n = len(arr)
answer = next_greater_element_to_right(arr,n)
print("answer", answer)
