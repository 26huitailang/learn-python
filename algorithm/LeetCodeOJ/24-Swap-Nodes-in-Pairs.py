# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 涉及三个元素的指针交换，两个相邻元素和前一个元素的指针
        pre, pre.next = self, head
        while pre.next and pre.next.next:  # 相邻的两个元素存在
            # from pre -> a -> b -> b.next
            # to pre -> b -> a -> a.next
            a = pre.next
            b = pre.next.next
            pre.next, pre.next.next, a.next = b, a, b.next
            pre = a  # 相邻两个元素的前一个元素
        return self.next
