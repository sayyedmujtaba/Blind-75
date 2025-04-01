from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        longest = 0
        
        for n in numSet:  # Iterate over the set to avoid duplicate work
            if n - 1 not in numSet:  # Start of a new sequence
                length = 1
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)
                
        return longest
