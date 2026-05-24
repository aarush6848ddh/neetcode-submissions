class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                length += 1
            if length > 0:
                if not s[i].isalnum():
                    return length
        return length