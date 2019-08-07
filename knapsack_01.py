#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ShenHengheng
# @File    : knapsack_01.py
# @Desc    : 01 背包问题
# @Site:   :

"""
Problem: Given a knapsack with a total weight
capacity and a list of items with weight w(i)
and value v(i), determine which items to select
to maximize total value.

    total_weight = 8
    items
      v | w
      0 | 0
    a 2 | 2
    b 4 | 2
    c 6 | 4
    d 9 | 5

    max value = 13
    items
      v | w
    b 4 | 2
    d 9 | 5

"""

class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)


class Knapsack(object):

    def fill_knapsack(self, input_items, total_weight):

        pass