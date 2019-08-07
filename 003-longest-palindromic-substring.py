"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            raise TypeError("input cannot be none")

        

    def longestPalindromeBrute(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            raise TypeError("input cannot be none")

        res = ""
        for i in range(len(s)):
            j = i + 1
            while j <= len(s) and len(res) <= len(s[i:]):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                    res = s[i:j]
                j+=1

        return res

