# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next

        return val_list == val_list[::-1]
