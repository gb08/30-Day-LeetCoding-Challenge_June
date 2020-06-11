"""
Problem:
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.
"""
# Solution:

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        ch = [0] * (amount + 1)
        ch[0] = 1
        for i in coins:
            for j in range(i, amount + 1):
                ch[j] = ch[j-i] + ch[j]
        return ch[-1]
