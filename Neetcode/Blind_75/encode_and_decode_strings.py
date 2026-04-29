"""
Encode and Decode Strings
Difficulty: Medium

Description:
    Design an algorithm to encode a list of strings to a single string, then
    decode that string back to the original list. Encoding uses a length prefix
    followed by a delimiter: e.g. ["lint", "code"] -> "4!lint4!code".

encode Args:    strs (List[str]): List of strings to encode.
encode Returns: str: A single encoded string representing the list.

decode Args:    s (str): Encoded string produced by encode().
decode Returns: List[str]: The original list of strings.

Time Complexity:  O(n * m) — n strings each of max length m
Space Complexity: O(n * m)
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
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
