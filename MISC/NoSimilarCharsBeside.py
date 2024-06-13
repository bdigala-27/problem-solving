from heapq import heappush, heappop
from collections import Counter


def reorganizeString(s):
    if not s:
        return ""

    # Count the frequency of each character
    freq = Counter(s)

    # Create a max-heap based on the frequencies (negative values for max-heap in Python)
    max_heap = []
    for char, count in freq.items():
        heappush(max_heap, (-count, char))

    # Variables to store the previous character and its frequency
    prev_count, prev_char = 0, ''
    result = []

    while max_heap:
        # Get the character with the highest frequency
        count, char = heappop(max_heap)
        # Append it to the result
        result.append(char)

        # Since we're using a max-heap with negative values, increase the count towards zero
        count += 1  # This means we used one instance of this character

        # If the previous character's count is not zero, add it back to the heap
        if prev_count < 0:
            heappush(max_heap, (prev_count, prev_char))

        # Update previous character and its count
        prev_count, prev_char = count, char

    # Join the list to form the final shuffled string
    result_str = ''.join(result)

    # If the length of the result string is not equal to the input string, it means reorganization was not possible
    if len(result_str) != len(s):
        return ""

    return result_str


# Example usage
s = ['a', 'a', 'b', 'b', 'c', 'c']
result = reorganizeString(s)
print("Shuffled array:", result)
