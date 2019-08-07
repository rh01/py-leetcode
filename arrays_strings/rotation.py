#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ShenHengheng
# @File    : rotation.py
# @Desc    :
# @Site:   :


"""
Constraints
==========
    Can we assume the string is ASCII?
    Yes
    Note: Unicode strings could require special handling depending on your language
    Is this case sensitive?
    Yes
    Can we use additional data structures?
    Yes
    Can we assume this fits in memory?
    Yes

Test Cases
==========

- Any strings that differ in size -> False
- None, 'foo' -> False (any None results in False)
- ' ', 'foo' -> False
- ' ', ' ' -> True
- 'foobarbaz', 'barbazfoo' -> True
"""

class Rotation(object):
    def is_substring(self, s1, s2):
        # TODO: Implement me
        return s2.find(s1) != -1

    def is_rotation(self, s1, s2):
        # TODO: Implement me
        # Call is_substring only once
        if s1 == None or s2 == None:
            return False
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False

        for i in range(len(s1)):
            if self.is_substring(s1[:i], s2) & self.is_substring(s1[i:], s2):
                return True

        return False
