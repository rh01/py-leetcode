#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ShenHengheng
# @File    : 015-threeSum.py
# @Desc    :
# @Site:   : https://leetcode.com/problems/3sum/

"""
    Given an array nums of n integers, are there elements
    a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

    Note:
    -----

    The solution set must not contain duplicate triplets.

    Example:
    -------

    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    ```
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
    ```
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort() # sort nums
        res = set()
        for idx, x in enumerate(nums[:-2]):
            if idx >= 1 and x == nums[idx-1]:
                continue
            d = {}

            for y in nums[idx+1:]:
                if y not in d:
                    d[-x-y] = 1
                else:
                    set.add(x, y, -x-y)
        return map(list, res)

    def threeSumLianBianJia(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # sort nums
        res = []
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1  # start
            k = len(nums) - 1  # end
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1;
                    k -= 1
        return res