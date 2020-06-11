"""
Problem:
Given an integer, write a function to determine if it is a power of two.
"""

# Solution

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n%2 == 0 and n>1:
            n = n/2
        return n==1
