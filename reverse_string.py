"""
Question:

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""


class Solution(object):
    # Approach 1:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        count = 0
        while count < len(s):
            s.insert(count, s.pop())
            count += 1
            
     # Approach 2:
     def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s)-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start +=1
            end -= 1

