#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ShenHengheng
# @File    : 011-ContainerWithMostWater.py
# @Desc    :
# @Site:   : https://leetcode.com/problems/container-with-most-water/

"""
    Given n non-negative integers a1, a2, ..., an, where each
    represents a point at coordinate(i, ai).n vertical lines
    are drawn such that the two endpoints of line i is at(i, ai) and (i, 0).Find
    two lines, which together with x - axis forms a container,
    such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.

    Example:
    ========

    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49
"""

import  sys

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        res = -sys.maxsize
        l = 0; r = len(height) - 1
        while l < r:
            res = max(res, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return res



    def maxAreaBrute(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        res = -sys.maxsize

        for i in range(len(height)):
            for j in range(i+1,len(height)):
                res = max(res, min(height[i], height[j])*(j-i))
        return res
