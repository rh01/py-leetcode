#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ShenHengheng
# @File    : 242-ValidAnagram.py
# @Desc    :
# @Site:   :


"""
    Given two strings s and t , write a function to determine if t is an anagram of s.

    Example 1:
    =========

    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:
    =========

    Input: s = "rat", t = "car"
    Output: false

"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False

        if len(s) != len(t):
            return False

        return sorted(s) ==sorted(t)

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
