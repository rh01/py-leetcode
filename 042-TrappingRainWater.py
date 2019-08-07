#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ShenHengheng
# @File    : 042-TrappingRainWater.py
# @Desc    :
# @Site:   : https://leetcode.com/problems/trapping-rain-water/

"""
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it is able to trap after raining.

    Example:
    ========
    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0

        idx_stack = []
        res, current = 0, 0
        while current < len(height):
            while len(idx_stack) != 0 and height[current] > height[idx_stack[-1]]:
                top = idx_stack[-1]
                idx_stack.pop()
                if len(idx_stack)==0:
                    break
                distance = current - idx_stack[-1] - 1
                bound = min(height[current], height[idx_stack[-1]] )- height[top]
                res += distance * bound

            idx_stack.append(current)
            current += 1
        return res
