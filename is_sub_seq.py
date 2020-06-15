"""
Problem:
Given a string s and a string t, check if s is subsequence of t.
A subsequence of a string is a new string which is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, "ace" is a subsequence of "abcde" while "aec" is not).
"""

# Solution
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
        elif len(s) == len(t) or (not t):
            return False

        pT, pS = 0, 0
        while pT<len(t) and pS<len(s) :
            if s[pS] == t[pT]:
                pS+=1
            pT+=1
        return pS==len(s)
