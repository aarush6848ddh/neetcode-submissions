class Solution:
    def scoreOfString(self, s: str) -> int:
        s_list = list(s)
        res = 0
        for i in range(len(s_list) - 1, 0, -1):
            res += abs(ord(s_list[i]) - ord(s_list[i - 1]))
        return res
