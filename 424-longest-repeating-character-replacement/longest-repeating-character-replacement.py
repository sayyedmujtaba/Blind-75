class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        max_value = 0
        output = 0

        for right in range(len(s)):
            right_char = s[right]
            seen[right_char] = seen.get(right_char, 0) + 1
            max_value = max(max_value, seen[right_char])

            while (right - left + 1) - max_value > k:
                seen[s[left]] -= 1
                left += 1

            output = max(output, right - left + 1)

        return output
