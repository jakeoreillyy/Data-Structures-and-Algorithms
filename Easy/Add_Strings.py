"""
Add Strings
Leetcode Problem: 415
Difficulty: Easy
Description: Given two non-negative integers, num1 and num2 represented as strings, return the sum of num1 and num2 as a string. i.e. num1 = "11", num2 = "123" returns "134"
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            a = 0
            b = 0

            if i >= 0:
                # alternative: a = ord(num1[i]) - ord('0')
                a = int(num1[i])
            if j >= 0:
                # alternative: b = ord(num2[j]) - ord('0')git  
                b = int(num2[j])
            
            i -= 1
            j -= 1

            total = a + b + carry
            carry = total // 10
            result.append(str(total % 10))

        return ''.join(reversed(result))