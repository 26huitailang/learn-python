# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, cur = None, head

        while cur:
            # 分解：
            # 1. 将cur的指针指向pre
            # 2. 下一个pre换成cur
            # 3. 下一个cur是当下cur指针指向的节点
            cur.next, pre, cur = pre, cur, cur.next
        return pre
