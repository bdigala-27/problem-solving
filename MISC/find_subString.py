def findSubstrings(s):
    n = len(s)
    seen = set()
    count = 0

    left = 0
    for right in range(n):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        count += right - left + 1

    return count


# Example usage:
s = "bcada"
print(findSubstrings(s))