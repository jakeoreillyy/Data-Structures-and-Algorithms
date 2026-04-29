"""
Encode and Decode Strings
Difficulty: Medium
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. e.g. The string "lint" is encoded to "4#lint", where the length of the string is 4. So the list ["lint", "code", "love", "you"] is encoded to "4#lint4#code4#love3#you". Note that one can encode any possible string as long as it follows the above algorithm. The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "!" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "!":
                j +=1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res