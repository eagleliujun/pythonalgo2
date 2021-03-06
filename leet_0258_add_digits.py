"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one
digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0

        return (num - 1) % 9 + 1

    def addDigits_rec(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            res = 0
            for digit in str(num):
                res += int(digit)
            return self.addDigits(res)
