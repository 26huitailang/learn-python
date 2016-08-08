#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur.next != None and cur != None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# [1,1,1,2,2,2,3,3,3]
# expected [1, 2, 3]