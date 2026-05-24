class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join([char for char in s if char.isalnum()])
        lower_s = new_s.lower()
        print(lower_s)
        if lower_s[::-1] == lower_s:
            return True
        return False