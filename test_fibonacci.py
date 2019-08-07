#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ShenHengheng
# @File    : test_fibonacci.py.py
# @Desc    :
# @Site:   :

import unittest
from xxx_fibonacci import Math

class TestMath(unittest.TestCase):
    math = Math()
    def test_fib(self, func=math.fib_dynamic):

        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(func(i))
        self.assertEquals(result, expected)
        print('Success: test_fib')

    def test_fib2(self, func=math.fib_iterative):

        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(func(i))
        self.assertEquals(result, expected)
        print('Success: test_fib')

    def test_fib3(self, func=math.fib_dynamic):

        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(func(i))
        self.assertEquals(result, expected)
        print('Success: test_fib')


# def main():
#     test = TestMath()
#     math = Math()
#     test.test_fib(math.fib_recursive)
#     test.test_fib(math.fib_dynamic)
#     test.test_fib(math.fib_iterative)


if __name__ == '__main__':
    unittest.main()