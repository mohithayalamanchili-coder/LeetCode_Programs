class Solution:
    def checkString(self, s: str) -> bool:
        foundB = False
        for ch in s:
            if ch == 'b':
                foundB = True
            if ch == 'a' and foundB:
                return False
        return True