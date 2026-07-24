import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        split = re.split(r"\W+", s.lower())
        helper = "".join(split)

        p1 = 0
        p2 = len(helper) - 1

        length = int(len(helper)/2)

        for k in range(length):
            if (helper[p1] != helper[p2]):
                return False

            p1 += 1
            p2 -= 1

        return True
