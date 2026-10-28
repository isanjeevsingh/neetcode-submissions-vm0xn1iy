class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            ascii_code = [0] * 26
            for c in s:
                ascii_code[ord(c)-ord('a')] += 1
            res[tuple(ascii_code)].append(s)
        return list(res.values())