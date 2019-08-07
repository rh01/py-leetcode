#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ShenHengheng
# File  : 703-kth-largest_element-in-a-stream-pq.py

import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = list()
        self.k = k
        #self.cap = k

        #self.nums = sorted(nums, reverse=True)
        for num in nums:
            self._add(num)

    def _add(self, num):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, num)
        else:
            if num > self.heap[0]:
                heapq.heapreplace(self.heap, num)




    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self._add(val)
        return self.heap[0]



