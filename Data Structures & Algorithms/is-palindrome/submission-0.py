import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        helper = re.split(r"\W+", s.lower())

        new_s = "".join(helper)
        reverse_s = new_s[::-1]

        if new_s == reverse_s:
            return True

        return False