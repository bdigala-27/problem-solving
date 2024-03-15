'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''


nums = [4,5,6,7,0,1,2]
target = 0
def search(nums, target):
    low,high =0,len(nums)-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        if nums[low]<=nums[mid]:
            if nums[low]<=target<nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if nums[mid]<target<=nums[high]:
                low=mid+1
            else:
                high = mid-1
    return -1
print(search(nums,target))

#Extra points to add:

'''
Built in Index method uses the Binary search algorithm for the sorted list or else it implements the linear search algorithm. so for the sorted array(it implements the O(logn) for linear search it implements the O(n))

Yes, the built-in `index` method in Python for lists has a time complexity of O(log n) on average for sorted lists.

The `index` method internally uses a variant of the binary search algorithm to find the target element in the sorted list. The binary search algorithm has an average time complexity of O(log n) because it halves the search space in each iteration.

However, in the worst case, when the target element is not present in the list or when the list is not sorted, the `index` method will have to perform a linear search, which would result in a time complexity of O(n).

Additionally, it's worth noting that the `index` method has a few advantages over the manual implementation of binary search:

1. **It's built-in**: You don't need to write and maintain the binary search logic yourself, which can reduce the chances of bugs and make your code more readable.

2. **It handles edge cases**: The built-in implementation handles edge cases such as empty lists, which you would have to handle manually in your implementation.

3. **It can be more efficient**: The built-in implementation is likely to be more efficient than a manual implementation, as it's written in lower-level language (C) and optimized for performance.

That being said, if you want to have more control over the algorithm or if you need to handle specific edge cases or variations of the binary search problem, a manual implementation might be preferred.

In summary, yes, the built-in `index` method for sorted lists in Python has an average time complexity of O(log n), making it a efficient option for searching in sorted lists.
'''


'''
No, the built-in `index` method in Python will not implement an O(log n) time complexity for searching in a rotated sorted array. The `index` method assumes that the list is entirely sorted in ascending order.

When dealing with a rotated sorted array, where the array is sorted but rotated at some pivot point, the built-in `index` method will perform a linear search, resulting in a time complexity of O(n).

Here's an example to illustrate this:

```python
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(nums.index(target))  # Output: 4
```

In this case, the `index` method will start searching from the beginning of the list and linearly check each element until it finds the target element `0` at index `4`. This linear search has a time complexity of O(n), where n is the length of the list.

To solve the problem of searching in a rotated sorted array with an O(log n) time complexity, you need to implement a modified version of the binary search algorithm that takes the rotation into account.

Here's an example implementation:

```python
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(search(nums, target))  # Output: 4
```

This modified binary search algorithm checks if the left or right portion of the array is sorted and performs the binary search within the sorted portion. 
This approach maintains the O(log n) time complexity for searching in a rotated sorted array.

To summarize, while the built-in `index` method in Python is efficient for searching in a completely sorted array, 
it does not maintain the O(log n) time complexity for searching in a rotated sorted array. 
In such cases, you need to implement a modified binary search algorithm tailored for rotated sorted arrays.
'''