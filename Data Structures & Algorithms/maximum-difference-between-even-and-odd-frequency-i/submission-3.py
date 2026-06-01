class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0]*26
        for c in s:
            freq[ord(c) - ord("a")] += 1
        odd = max([x for x in freq if x % 2 == 1 and x != 0])
        even = min([x for x in freq if x % 2 == 0 and x != 0])
        return odd - even