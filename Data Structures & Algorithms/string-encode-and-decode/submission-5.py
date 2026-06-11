class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty_list"
        return "@*!".join(strs)
        

    def decode(self, s: str) -> List[str]:
        if s == "empty_list":
            return []
        return s.split("@*!")