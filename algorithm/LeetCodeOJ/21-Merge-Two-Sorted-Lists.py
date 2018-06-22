# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        tmp = ret
        while True:
            if l1 is None:  # 如果l1到头，那么next往后就是l2
                tmp.next = l2
                break
            elif l2 is None:
                tmp.next = l1
                break
            
            if l1.val < l2.val:  # l1当前值小于l2
                tmp.next = l1  # tmp下一个点为小一点的值
                tmp = tmp.next  # 向前移动一位
                l1 = l1.next  # 向前移动一位
            else:
                tmp.next = l2
                tmp = tmp.next
                l2 = l2.next
        # 初始节点是0，返回它的下一个点
        return ret.next
                