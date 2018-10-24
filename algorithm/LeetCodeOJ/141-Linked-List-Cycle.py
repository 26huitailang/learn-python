"""
1. 可以用set存储已经访问的元素，如果遇到相同的，说明已经存在
2. 快慢指针，相遇表示有环
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while slow and fast and fast.next:  # 确保fast.next.next不出错
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False