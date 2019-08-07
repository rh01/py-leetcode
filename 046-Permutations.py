#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ShenHengheng
# @File    : 046-Permutations.py
# @Desc    :
# @Site:   : https://leetcode.com/problems/permutations/
"""

Given a collection of distinct integers, return all possible permutations.

Example:
===========

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []
        self.res = []
        self._permute(nums, [])

        return self.res


    def _permute(self, nums, arr):

        if not nums:
            self.res.append(arr)
            return

        for i in range(len(nums)):
            tmp = nums[i]
            nums.pop(i)
            self._permute(nums, arr+[tmp])
            nums.insert(i, tmp)
