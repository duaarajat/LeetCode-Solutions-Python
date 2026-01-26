"""Given two strings s and t, return true if t is an anagram of s, and false otherwise."""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        char_count = {}
        for i in s:
            char_count[i] = char_count.get(i, 0) + 1
            
        for j in t:
            if j not in char_count or char_count[j] == 0:
                return False
            char_count[j] -= 1
            
        return True

sol=Solution()
s = input("Enter a string: ")
t = input("Enter same length string: ")
print(sol.isAnagram(s,t))