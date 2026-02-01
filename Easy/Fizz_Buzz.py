"""
Fizz Buzz
LeetCode problem: 412
Difficulty: Easy
Description: Returns a list of strings from 1 to n, replacing multiples of 3 with
             "Fizz", multiples of 5 with "Buzz", and multiples of both 3 ad 5 with
             "FizzBuzz"
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # initialize the answer list
        answer = []

        # loop through the all numbers from 1 to n
        for i in range(1, n+1):
            # if index is divisible by 3 and 5, will append FizzBuzz
            if i % 3 == 0 and i % 5 ==0:
                answer.append("FizzBuzz")
            # else if index is divisible by only 3, will append Fizz
            elif i % 3 == 0:
                answer.append("Fizz")
            # else if index is divisible by only 5, will append Buzz
            elif i % 5 == 0:
                answer.append("Buzz")
            # else otherwise, will append the number as a string
            else:
                answer.append(str(i))
        # return the final list
        return answer