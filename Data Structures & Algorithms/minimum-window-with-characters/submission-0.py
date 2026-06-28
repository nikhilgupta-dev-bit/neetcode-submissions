class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        mp2 = {}
        for c in t:
            mp2[c] = mp2.get(c, 0) + 1

        mp1 = {}

        required = len(mp2)
        formed = 0

        l = 0
        res = [-1, -1]
        min_length = float('inf')

        for r in range(len(s)):
            char = s[r]
            mp1[char] = mp1.get(char, 0) + 1

            if char in mp2 and mp1[char] == mp2[char]:
                formed += 1

            # shrink window
            while formed == required:
                if (r - l + 1) < min_length:
                    res = [l, r]
                    min_length = r - l + 1

                left_char = s[l]
                mp1[left_char] -= 1

                if left_char in mp2 and mp1[left_char] < mp2[left_char]:
                    formed -= 1

                l += 1

        l, r = res
        return s[l:r+1] if min_length != float('inf') else ""
