class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        c = 0
        l = []
        for i in s:
            if  i.isalnum():
                i = i.lower()
                l.append(i)
        return l[::] == l[::-1]

            