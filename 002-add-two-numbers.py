"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result = []
        while self:
            result.append(self.val)
            self = self.next
        return ','.join(map(str, result))

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        gw = (l1.val + l2.val) % 10
        first = ListNode(gw)
        result = first
        jw = (l1.val + l2.val) // 10

        l1 = l1.next
        l2 = l2.next


        while l1 is not None and l2 is not None:
            gw = (l1.val + l2.val + jw) % 10
            result.next = ListNode(gw)
            jw = (l1.val + l2.val + jw) // 10
            l1 = l1.next
            l2 = l2.next
            result = result.next


        while l1:
            gw = (l1.val + jw) % 10
            result.next = ListNode(gw)
            #result.next = ListNode(l1.val+ jw)
            result = result.next

            jw = (l1.val + jw) // 10
            l1 = l1.next

        while l2:
            gw = (l2.val + jw) % 10
            result.next = ListNode(gw)

            result = result.next

            jw = (jw+ l2.val) // 10
            l2 = l2.next


        if jw > 0:
            result.next = ListNode(jw)

        return first


s = Solution()
l1 = ListNode(9)
l1.next= ListNode(9)


l2 = ListNode(1)




print(s.addTwoNumbers(l1, l2))