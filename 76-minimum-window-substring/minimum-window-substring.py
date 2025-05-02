class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Build frequency map for t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        required = len(t_count)
        window_counts = {}

        l = 0
        formed = 0
        ans = [float('inf'), 0, 0]  # window length, left, right

        for r in range(len(s)):
            c = s[r]
            window_counts[c] = window_counts.get(c, 0) + 1

            if c in t_count and window_counts[c] == t_count[c]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = [r - l + 1, l, r]

                window_counts[s[l]] -= 1
                if s[l] in t_count and window_counts[s[l]] < t_count[s[l]]:
                    formed -= 1
                l += 1

        if ans[0] == float('inf'):
            return ""
        return s[ans[1]:ans[2]+1]
