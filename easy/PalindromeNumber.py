class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: return False
        if x == 0: return True
        if x % 10 == 0: return False
        r = 0
        n = x
        while n > 0:
            digit = n % 10
            r = r * 10 + digit
            n = n//10

        if r == x: return True
        else: return False
